---
name: image_to_image_lora_sampler_unet_45
type: Image To Image
frequency: 12
level: moderate
coverage: 0.956833
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2511任意姿态生成_2103492106114387969.json, 图片生成/图生图/Three-View Drawings三视图 qwen_image_edit_2511_2093148144774246401.json, 图片生成/图生图/qwen image edit_2070040758069063682.json, 图片生成/图生图/qwen2511移除主体_无痕局部重绘_消除指定物体__2067436200457236481.json, 图片生成/图生图/qwen2511移除主体_无痕局部重绘_消除指定物体__2067516185725460482.json, 图片生成/图生图/wink_2511__2028452743941197826.json, 图片生成/图生图/侧躺沙发 2511_2021541863076929538.json, 图片生成/图生图/卧室穿搭 2511_2028422039324856322.json, 图片生成/图生图/双图分镜 2511_2024081531601424385.json, 图片生成/图生图/提取服装为产品图 2511_2020424468195184642.json, 图片生成/图生图/穿上服装 2511_2020420989573664769.json, 图片生成/图生图/蹲拍 2511_2036798331170594817.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_45

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen2511任意姿态生成_2103492106114387969.json、图片生成/图生图/Three-View Drawings三视图 qwen_image_edit_2511_2093148144774246401.json、图片生成/图生图/qwen image edit_2070040758069063682.json、图片生成/图生图/qwen2511移除主体_无痕局部重绘_消除指定物体__2067436200457236481.json、图片生成/图生图/qwen2511移除主体_无痕局部重绘_消除指定物体__2067516185725460482.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGNorm`
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
- `ConditioningZeroOut` —— 11/12 个有
- `TextEncodeQwenImageEditPlus` —— 11/12 个有
- `ReferenceLatent` —— 10/12 个有
- `EmptyLatentImage` —— 9/12 个有
- `ImageScaleToTotalPixels` —— 7/12 个有
- `PIP_图像联结` —— 7/12 个有
- `JjkText` —— 4/12 个有
- `FluxKontextImageScale` —— 3/12 个有
- `Image Comparer (rgthree)` —— 2/12 个有
- `LatentUpscaleBy` —— 2/12 个有
- `PreviewAny` —— 2/12 个有
- `ComfySwitchNode` —— 1/12 个有
- `MultiTextConcatenate` —— 1/12 个有
- `QwenEditTextEncode_EditUtils` —— 1/12 个有
- `RH_Captioner` —— 1/12 个有
- `RH_LLMAPI_Pro_Node` —— 1/12 个有
- `ResolutionSelector` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 928 - 1664 | 9 | 77% |
| 高度 | 1080 | 928 - 1664 | 9 | 77% |
| 采样步数 | 4 | 4 - 20 | 12 | 15% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 928 - 1664，9 个样本
- 高度 中位数 1080，观测区间 928 - 1664，9 个样本
- 采样步数 中位数 4，观测区间 4 - 20，12 个样本，取值分散，一致性仅 15%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
