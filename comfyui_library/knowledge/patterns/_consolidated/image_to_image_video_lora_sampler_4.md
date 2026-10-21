---
name: image_to_image_video_lora_sampler_4
type: Image To Image
frequency: 7
level: strong
coverage: 0.485
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CRTFirstLastFrameSelector, Fast Groups Bypasser (rgthree), INTConstant, ImageBatchMulti, ImageConcatMulti, ImageResizeKJv2, ImageStitch, Int, JWStringConcat, JoinStrings, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PainterI2V, PathchSageAttentionKJ, PreviewImage, PrimitiveInt, ProcessString, Qwen3_VQA, RIFE VFI, SaveImage, ShowText|pysssss, Text Multiline, TextEncodeQwenImageEditPlus, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanMultiFrameRefToVideo, easy cleanGpuUsed, easy promptLine, easy showAnything, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/产品多分镜+多角度+多场景+单图_三图生视频_2002487518991925249.json, 视频生成/图生视频/1994300915066880001.json, 视频生成/图生视频/1996217524062666754.json, 视频生成/图生视频/1989240628179513346.json, 视频生成/图生视频/AI最强长视频流=多分镜+单图_首中尾帧出视频，清晰-慢-200RH_2082744677681418242.json, 视频生成/图生视频/2003367093624053762.json, 视频生成/图生视频/1996194043233255425.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/产品多分镜+多角度+多场景+单图_三图生视频_2002487518991925249.json、视频生成/图生视频/1994300915066880001.json、视频生成/图生视频/1996217524062666754.json、视频生成/图生视频/1989240628179513346.json、视频生成/图生视频/AI最强长视频流=多分镜+单图_首中尾帧出视频，清晰-慢-200RH_2082744677681418242.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：48%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CRTFirstLastFrameSelector`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `ImageBatchMulti`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `ImageStitch`
- `Int`
- `JWStringConcat`
- `JoinStrings`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PainterI2V`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveInt`
- `ProcessString`
- `Qwen3_VQA`
- `RIFE VFI`
- `SaveImage`
- `ShowText|pysssss`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMultiFrameRefToVideo`
- `easy cleanGpuUsed`
- `easy promptLine`
- `easy showAnything`
- `wanBlockSwap`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler_ancestral | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（14/7 个样本）：Steps较低可能导致细节不足
