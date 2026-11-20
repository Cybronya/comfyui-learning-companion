---
name: text_to_image_video_lora_sampler_202
type: Text To Image
frequency: 3
level: strong
coverage: 0.840667
common_nodes: [Bjornulf_ShowInt, CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, CR Integer To String, CreateCFGScheduleFloatList, EmptyLatentImage, GetImageSizeAndCount, ImageResizeKJv2, JWInteger, KSampler, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, LoraLoader, MathExpression|pysssss, PreviewImage, Primitive integer [Crystools], RHBatchImages:, RHHiddenNodes, RH_LLMAPI_NODE, SaveImage, ShowText|pysssss, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, Wan_video_prompt_generator, easy forLoopEnd, easy forLoopStart, easy imageCount]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/wan2.2批量视频生成器V3.1版本_1957653150733889537.json, 视频生成/文生视频/wan2.2批量视频生成器V3.2版本（可批量跳舞一次性20个）_1958383556336762882.json, 视频生成/文生视频/wan2.2批量视频生成器V3版本_1951108375138476034.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_202

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/wan2.2批量视频生成器V3.1版本_1957653150733889537.json、视频生成/文生视频/wan2.2批量视频生成器V3.2版本（可批量跳舞一次性20个）_1958383556336762882.json、视频生成/文生视频/wan2.2批量视频生成器V3版本_1951108375138476034.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Integer To String`
- `CreateCFGScheduleFloatList`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `JWInteger`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadWanVideoT5TextEncoder`
- `LoraLoader`
- `MathExpression|pysssss`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RHBatchImages:`
- `RHHiddenNodes`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `ShowText|pysssss`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `Wan_video_prompt_generator`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 2/3 个有
- `easy int` —— 2/3 个有
- `easy mathInt` —— 2/3 个有
- `easy showAnything` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.4 | 0.4 - 0.4 | 3 | 100% |
| LoRA 文本强度 | 0.4 | 0.4 - 0.4 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2s | - | 3 | 100% |
| 调度器 | bong_tangent | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.4，观测区间 0.4 - 0.4，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.4，观测区间 0.4 - 0.4，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，3 个样本，一致性 100%
- 调度器 最常用 bong_tangent，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
