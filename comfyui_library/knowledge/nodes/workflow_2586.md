# workflow>高清放大

## 节点类型

`workflow>高清放大`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `LoRA:PEFTLORA`（3 次）
- `模型:MODEL`（3 次）
- `图像:IMAGE`（3 次）
- `参考图像:IMAGE`（3 次）
- `VAE:VAE`（3 次）
- `CLIP:CLIP`（3 次）
- `VAE(可选):VAE`（3 次）
- `脚本:SCRIPT`（3 次）

## 输出

- `宽度:INT`（3 次）
- `高度:INT`（3 次）
- `图像:IMAGE`（3 次）
- `遮罩:MASK`（3 次）
- `json数据:JSON`（3 次）
- `模型:MODEL`（3 次）
- `正面条件:CONDITIONING`（3 次）
- `负面条件:CONDITIONING`（3 次）
- `KSampler (Efficient) 图像:IMAGE`（3 次）
- `output:*`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["4xNomos8kSCHAT-L.pth", "Florence-2-large", "fp16", "sdpa", false, 1024, 1024, "nearest-exact", true, 2, "disabled", "l`（1 次）
- `["4xNomos8kSCHAT-L.pth", "Florence-2-large", "fp16", "sdpa", false, 1024, 1024, "nearest-exact", true, 2, "disabled", "l`（1 次）
- `["Florence-2-large", "fp16", "sdpa", false, "4xNomos8kSCHAT-L.pth", 1024, 1024, "nearest-exact", true, 2, "disabled", "l`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
