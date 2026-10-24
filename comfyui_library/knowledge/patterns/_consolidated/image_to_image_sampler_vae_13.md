---
name: image_to_image_sampler_vae_13
type: Image To Image
frequency: 10
level: moderate
coverage: 0.907
common_nodes: [CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Nunchaku-Qwen-Image-ControlNet-Inpainting 局部重绘_2073059743991681026.json, 图片生成/图生图/Nunchaku-Qwen-Image-Edit_1965891895425699842.json, 图片生成/图生图/QWen-Image 局部重绘_1966848954535174146.json, 图片生成/图生图/Qwen Edit 4步 加速 图像编辑_1967372813134913537.json, 图片生成/图生图/Qwen Edit 8步加速 图像编辑_1967376109622976514.json, 图片生成/图生图/Qwen Edit 图像编辑 Canny 控制_1968183874985537537.json, 图片生成/图生图/Qwen Edit 图像编辑 Depth 控制_1968182929035788290.json, 图片生成/图生图/Qwen Edit 图像编辑 OpenPose 控制_1968011303954579458.json, 图片生成/图生图/Qwen Edit+姿势-图像精准编辑控制V1_1961275242461249538.json, 图片生成/图生图/Qwen Edit+深度精准编辑控制V1_1961284446211215362.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_13

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Nunchaku-Qwen-Image-ControlNet-Inpainting 局部重绘_2073059743991681026.json、图片生成/图生图/Nunchaku-Qwen-Image-Edit_1965891895425699842.json、图片生成/图生图/QWen-Image 局部重绘_1966848954535174146.json、图片生成/图生图/Qwen Edit 4步 加速 图像编辑_1967372813134913537.json、图片生成/图生图/Qwen Edit 8步加速 图像编辑_1967376109622976514.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 9/10 个有
- `CFGNorm` —— 8/10 个有
- `TextEncodeQwenImageEdit` —— 8/10 个有
- `UNETLoader` —— 8/10 个有
- `ControlNetLoader` —— 7/10 个有
- `ControlNetApplySD3` —— 5/10 个有
- `JjkText` —— 5/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `SetUnionControlNetType` —— 5/10 个有
- `ImageConcanate` —— 4/10 个有
- `ImageConcatMulti` —— 3/10 个有
- `CLIPTextEncode` —— 2/10 个有
- `CR Prompt Text` —— 2/10 个有
- `ControlNetInpaintingAliMamaApply` —— 2/10 个有
- `NunchakuQwenImageDiTLoader` —— 2/10 个有
- `OpenposePreprocessor` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `CannyEdgePreprocessor` —— 1/10 个有
- `DepthAnythingV2Preprocessor` —— 1/10 个有
- `DepthAnything_V2` —— 1/10 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 30 | 10 | 46% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 10 | 61% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| ControlNet 权重 | 1.5 | 1.5 - 2 | 5 | 88% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 30，10 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1.5，观测区间 1.5 - 2，5 个样本，取值集中（一致性 88%）
