---
name: unknown_workflow_video_clip_unet_3
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.876412
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1981260473284943874.json, 视频生成/图生视频/1980195972468871170.json, 视频生成/图生视频/1979525930601320449.json, 视频生成/图生视频/1983826871899070465.json, 视频生成/图生视频/1996163879166263297.json, 视频生成/图生视频/2017121557004423170.json, 视频生成/图生视频/2000048789195026433.json, 视频生成/图生视频/2000389959175503873.json, 视频生成/图生视频/2054151645621178370.json, 视频生成/图生视频/2000759932968464386.json, 视频生成/图生视频/2000116750941384705.json, 视频生成/图生视频/2000091759243915265.json, 视频生成/图生视频/2009529023986147330.json, 视频生成/图生视频/2012907856802095105.json, 视频生成/图生视频/2010234636823175169.json, 视频生成/图生视频/2015353958482579458.json, 视频生成/图生视频/2009591518486601729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_3

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/1981260473284943874.json、视频生成/图生视频/1980195972468871170.json、视频生成/图生视频/1979525930601320449.json、视频生成/图生视频/1983826871899070465.json、视频生成/图生视频/1996163879166263297.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 16/17 个有
- `CLIPVisionLoader` —— 16/17 个有
- `easy cleanGpuUsed` —— 16/17 个有
- `wanBlockSwap` —— 16/17 个有
- `ImpactInt` —— 15/17 个有
- `KSamplerAdvanced` —— 15/17 个有
- `RIFE VFI` —— 15/17 个有
- `SimpleMath+` —— 15/17 个有
- `ModelSamplingSD3` —— 14/17 个有
- `PrimitiveStringMultiline` —— 13/17 个有
- `WanFirstLastFrameToVideo` —— 13/17 个有
- `Fast Bypasser (rgthree)` —— 12/17 个有
- `ImageScaleBy` —— 12/17 个有
- `Seed (rgthree)` —— 12/17 个有
- `JWInteger` —— 11/17 个有
- `Mute / Bypass Repeater (rgthree)` —— 11/17 个有
- `easy anythingIndexSwitch` —— 11/17 个有
- `easy batchAnything` —— 11/17 个有
- `easy forLoopEnd` —— 11/17 个有
- `easy forLoopStart` —— 11/17 个有
- `GetNode` —— 5/17 个有
- `SetNode` —— 5/17 个有
- `LoadAudio` —— 4/17 个有
- `PreviewImage` —— 4/17 个有
- `WanImageToVideo` —— 4/17 个有
- `ImageBatchGet` —— 3/17 个有
- `LoraLoaderModelOnly` —— 3/17 个有
- `SaveImage` —— 3/17 个有
- `easy imageSplitGrid` —— 3/17 个有
- `INTConstant` —— 2/17 个有
- `ImageConcatMulti` —— 2/17 个有
- `RH_Nano_Banana2_Image2Image` —— 2/17 个有
- `WanMoeKSampler` —— 2/17 个有
- `easy clearCacheAll` —— 2/17 个有
- `AILab_QwenVL_Advanced` —— 1/17 个有
- `CR Text Concatenate` —— 1/17 个有
- `Fooocus positive` —— 1/17 个有
- `ImageResize+` —— 1/17 个有
- `RH_Nano_Banana_Image2Image` —— 1/17 个有
- `RH_Translator` —— 1/17 个有
- `TT_img_enc` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 17 | 76% |
| Prompt 约束强度(CFG) | 6 | 6 - 20 | 17 | 47% |
| 采样算法 | 1 | 1 - 1 | 17 | 100% |
| 调度器 | euler_ancestral | - | 17 | 65% |
| 重绘幅度 | simple | - | 17 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，17 个样本，一致性 76%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 20，17 个样本，取值分散，一致性仅 47%
- 采样算法 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，17 个样本，一致性 65%
- 重绘幅度 最常用 simple，17 个样本，一致性 88%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
