---
name: image_to_image_lora_sampler_unet_57
type: Image To Image
frequency: 10
level: weak
coverage: 0.9558
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2511任意姿态生成_2103492106114387969.json, 图片生成/图生图/Three-View Drawings三视图 qwen_image_edit_2511_2093148144774246401.json, 图片生成/图生图/qwen image edit_2070040758069063682.json, 图片生成/图生图/qwen2511移除主体_无痕局部重绘_消除指定物体__2067436200457236481.json, 图片生成/图生图/qwen2511移除主体_无痕局部重绘_消除指定物体__2067516185725460482.json, 图片生成/图生图/wink_2511__2028452743941197826.json, 图片生成/图生图/【乐导】Qwen-Image-Edit-2509升级Plus版nunchaku加速_1992133522697809922.json, 图片生成/图生图/侧躺沙发 2511_2021541863076929538.json, 图片生成/图生图/卧室穿搭 2511_2028422039324856322.json, 图片生成/文生图/轮回插画风格 2511_2026075574397050881.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_57

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen2511任意姿态生成_2103492106114387969.json、图片生成/图生图/Three-View Drawings三视图 qwen_image_edit_2511_2093148144774246401.json、图片生成/图生图/qwen image edit_2070040758069063682.json、图片生成/图生图/qwen2511移除主体_无痕局部重绘_消除指定物体__2067436200457236481.json、图片生成/图生图/qwen2511移除主体_无痕局部重绘_消除指定物体__2067516185725460482.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 9/10 个有
- `ConditioningZeroOut` —— 9/10 个有
- `TextEncodeQwenImageEditPlus` —— 9/10 个有
- `EmptyLatentImage` —— 7/10 个有
- `ReferenceLatent` —— 7/10 个有
- `ImageScaleToTotalPixels` —— 5/10 个有
- `PIP_图像联结` —— 4/10 个有
- `FluxKontextImageScale` —— 3/10 个有
- `Image Comparer (rgthree)` —— 3/10 个有
- `JjkText` —— 3/10 个有
- `LatentUpscaleBy` —— 2/10 个有
- `ComfySwitchNode` —— 1/10 个有
- `NunchakuQwenImageDiTLoader` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `QwenEditTextEncode_EditUtils` —— 1/10 个有
- `RH_LLMAPI_Pro_Node` —— 1/10 个有
- `ResolutionSelector` —— 1/10 个有
- `UnetLoaderGGUF` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1664 | 7 | 68% |
| 高度 | 1024 | 512 - 1664 | 7 | 68% |
| 采样步数 | 6 | 4 - 20 | 10 | 30% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 10 | 34% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1664，7 个样本
- 高度 中位数 1024，观测区间 512 - 1664，7 个样本
- 采样步数 中位数 6，观测区间 4 - 20，10 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，10 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（8/10 个样本）：Steps较低可能导致细节不足
