# %%
import scanpy as sc
# %%
import sys
import torch

def check_gpu():
    print("=" * 60)
    print("环境信息")
    print("=" * 60)
    print(f"Python  : {sys.version.split()[0]}")
    print(f"PyTorch : {torch.__version__}")
    print(f"CUDA(编译版本): {torch.version.cuda}")

    print("\n" + "=" * 60)
    print("1. CUDA 可用性检查")
    print("=" * 60)
    cuda_available = torch.cuda.is_available()
    print(f"torch.cuda.is_available() -> {cuda_available}")

    if not cuda_available:
        print("\n❌ GPU 不可用。常见原因：")
        print("  - 安装的是 CPU 版 PyTorch（torch 版本号无 +cuXXX）")
        print("  - 未安装显卡驱动 / 驱动版本过低")
        print("  - CUDA 版本与驱动不匹配")
        return

    print(f"cuDNN   : {torch.backends.cudnn.version()}")
    print(f"GPU 数量: {torch.cuda.device_count()}")

    for i in range(torch.cuda.device_count()):
        props = torch.cuda.get_device_properties(i)
        print(f"\n  [GPU {i}] {torch.cuda.get_device_name(i)}")
        print(f"    显存      : {props.total_memory / 1024**3:.2f} GB")
        print(f"    计算能力  : {props.major}.{props.minor}")
        print(f"    多处理器数: {props.multi_processor_count}")

    print("\n" + "=" * 60)
    print("2. 实际张量运算测试（真正占一次显存）")
    print("=" * 60)
    try:
        device = torch.device("cuda:0")
        x = torch.randn(4096, 4096, device=device)
        y = torch.randn(4096, 4096, device=device)
        z = torch.matmul(x, y)          # 触发一次 GPU 计算
        torch.cuda.synchronize()        # 等待异步计算完成
        print(f"矩阵乘法完成，结果 shape={tuple(z.shape)}, device={z.device}")

        # 回传到 CPU 再核对一次
        assert z.is_cuda
        print(f"显存占用: {torch.cuda.memory_allocated(0) / 1024**2:.1f} MB")
        print("\n✅ GPU 可正常使用")
    except Exception as e:
        print(f"\n❌ GPU 计算失败: {type(e).__name__}: {e}")

if __name__ == "__main__":
    check_gpu()
# %%
