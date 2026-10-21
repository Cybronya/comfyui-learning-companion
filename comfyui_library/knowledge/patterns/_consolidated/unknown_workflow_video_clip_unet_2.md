---
name: unknown_workflow_video_clip_unet_2
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.908667
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, ImpactInt, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1981260473284943874.json, 视频生成/图生视频/1980195972468871170.json, 视频生成/图生视频/1979525930601320449.json, 视频生成/图生视频/1983826871899070465.json, 视频生成/图生视频/1987894798759735297.json, 视频生成/图生视频/1981343312810598402.json, 视频生成/图生视频/2000048789195026433.json, 视频生成/图生视频/2000389959175503873.json, 视频生成/图生视频/2054151645621178370.json, 视频生成/图生视频/2000759932968464386.json, 视频生成/图生视频/2000116750941384705.json, 视频生成/图生视频/2000091759243915265.json, 视频生成/图生视频/2009529023986147330.json, 视频生成/图生视频/2012907856802095105.json, 视频生成/图生视频/2010234636823175169.json, 视频生成/图生视频/2015353958482579458.json, 视频生成/图生视频/1981307265980555265.json, 视频生成/图生视频/1988425926365110274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_2

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/1981260473284943874.json、视频生成/图生视频/1980195972468871170.json、视频生成/图生视频/1979525930601320449.json、视频生成/图生视频/1983826871899070465.json、视频生成/图生视频/1987894798759735297.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `ImpactInt`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 17/18 个有
- `CLIPVisionLoader` —— 17/18 个有
- `easy cleanGpuUsed` —— 17/18 个有
- `wanBlockSwap` —— 17/18 个有
- `PrimitiveStringMultiline` —— 16/18 个有
- `RIFE VFI` —— 16/18 个有
- `Fast Bypasser (rgthree)` —— 15/18 个有
- `ModelSamplingSD3` —— 15/18 个有
- `Seed (rgthree)` —— 15/18 个有
- `Mute / Bypass Repeater (rgthree)` —— 14/18 个有
- `easy batchAnything` —— 14/18 个有
- `easy forLoopEnd` —— 14/18 个有
- `easy forLoopStart` —— 14/18 个有
- `KSamplerAdvanced` —— 12/18 个有
- `ImageScaleBy` —— 11/18 个有
- `JWInteger` —— 10/18 个有
- `WanFirstLastFrameToVideo` —— 10/18 个有
- `easy anythingIndexSwitch` —— 10/18 个有
- `WanImageToVideo` —— 8/18 个有
- `WanMoeKSampler` —— 6/18 个有
- `GetImageSizeAndCount` —— 4/18 个有
- `ImageFromBatch` —— 4/18 个有
- `MathExpression|pysssss` —— 4/18 个有
- `String Literal` —— 4/18 个有
- `Text Load Line From File` —— 4/18 个有
- `GetNode` —— 3/18 个有
- `LoadAudio` —— 3/18 个有
- `SetNode` —— 3/18 个有
- `ImageBatchGet` —— 2/18 个有
- `PreviewImage` —— 2/18 个有
- `SaveImage` —— 2/18 个有
- `easy imageSplitGrid` —— 2/18 个有
- `ImageResize+` —— 1/18 个有
- `LoraLoaderModelOnly` —— 1/18 个有
- `Note Plus (mtb)` —— 1/18 个有
- `RH_LLMAPI_NODE` —— 1/18 个有
- `RH_Nano_Banana2_Image2Image` —— 1/18 个有
- `RH_Nano_Banana_Image2Image` —— 1/18 个有
- `RH_Translator` —— 1/18 个有
- `easy showAnything` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 18 | 56% |
| Prompt 约束强度(CFG) | 6 | 6 - 20 | 18 | 46% |
| 采样算法 | 1 | 1 - 1 | 18 | 100% |
| 调度器 | euler_ancestral | - | 18 | 50% |
| 重绘幅度 | simple | - | 18 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，18 个样本，一致性 56%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 20，18 个样本，取值分散，一致性仅 46%
- 采样算法 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，18 个样本，一致性 50%
- 重绘幅度 最常用 simple，18 个样本，一致性 67%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
