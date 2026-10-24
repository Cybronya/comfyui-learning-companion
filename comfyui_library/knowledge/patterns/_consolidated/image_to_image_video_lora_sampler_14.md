---
name: image_to_image_video_lora_sampler_14
type: Image To Image
frequency: 3
level: strong
coverage: 0.907333
common_nodes: [CFGNorm, CLIPLoader, GetImageSizeAndCount, ImageResizeKJv2, ImageScaleToTotalPixels, KSampler, LoadImage, LoadWanVideoT5TextEncoder, ModelSamplingAuraFlow, PrimitiveInt, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/千问edit三分镜图+Wan2.2图生三分镜视频_1987004381801418754.json, 视频生成/图生视频/千问生成尾帧+Wan2.2首尾帧视频生成可自动提示词_1977963460321497090.json, 视频生成/图生视频/同一场景自定义姿势首尾帧视频_1971550971262398465.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_14

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/千问edit三分镜图+Wan2.2图生三分镜视频_1987004381801418754.json、视频生成/图生视频/千问生成尾帧+Wan2.2首尾帧视频生成可自动提示词_1977963460321497090.json、视频生成/图生视频/同一场景自定义姿势首尾帧视频_1971550971262398465.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `AILab_MiniCPM_4_V_Advanced` —— 2/3 个有
- `CLIPVisionLoader` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `CR Text Concatenate` —— 2/3 个有
- `ImageBatchMultiple+` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `WanVideoClipVisionEncode` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `CR Latent Batch Size` —— 1/3 个有
- `JWStringGetLine` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `MaskToImage` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `ProcessString` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `String` —— 1/3 个有
- `easy imageChooser` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta57 | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta57，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
