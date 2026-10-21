---
name: unknown_workflow_video_sampler_clip_34
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.977692
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, Fast Bypasser (rgthree), ImageResizeKJv2, ImpactInt, KSamplerAdvanced, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, Seed (rgthree), SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2004053514764599297.json, 视频生成/图生视频/1980432616040148994.json, 视频生成/图生视频/1983880606536925186.json, 视频生成/图生视频/2010998394537381889.json, 视频生成/图生视频/2035897809894903809.json, 视频生成/图生视频/2039617670403858433.json, 视频生成/图生视频/2041028074229211137.json, 视频生成/图生视频/1980633692215361538.json, 视频生成/图生视频/2006925723407228930.json, 视频生成/图生视频/2009598515076407298.json, 视频生成/图生视频/2009591518486601729.json, 视频生成/图生视频/2009284920207745026.json, 视频生成/图生视频/2017792462663716865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2004053514764599297.json、视频生成/图生视频/1980432616040148994.json、视频生成/图生视频/1983880606536925186.json、视频生成/图生视频/2010998394537381889.json、视频生成/图生视频/2035897809894903809.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `Fast Bypasser (rgthree)`
- `ImageResizeKJv2`
- `ImpactInt`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `Seed (rgthree)`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 11/13 个有
- `PrimitiveStringMultiline` —— 11/13 个有
- `RIFE VFI` —— 11/13 个有
- `WanImageToVideo` —— 8/13 个有
- `WanFirstLastFrameToVideo` —— 5/13 个有
- `LoadAudio` —— 4/13 个有
- `easy batchAnything` —— 4/13 个有
- `easy forLoopEnd` —— 4/13 个有
- `easy forLoopStart` —— 4/13 个有
- `JWInteger` —— 3/13 个有
- `RHHiddenNodes` —— 3/13 个有
- `easy anythingIndexSwitch` —— 3/13 个有
- `CR Text Concatenate` —— 2/13 个有
- `ImageBatchGet` —— 2/13 个有
- `easy imageSplitGrid` —— 2/13 个有
- `AILab_QwenVL_Advanced` —— 1/13 个有
- `Fooocus positive` —— 1/13 个有
- `LoraLoaderModelOnly` —— 1/13 个有
- `RH_Nano_Banana2_Image2Image` —— 1/13 个有
- `easy imageIndexSwitch` —— 1/13 个有
- `easy showAnything` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 13 | 77% |
| Prompt 约束强度(CFG) | 6 | 6 - 16 | 13 | 55% |
| 采样算法 | 1 | 1 - 1 | 13 | 100% |
| 调度器 | euler_ancestral | - | 13 | 69% |
| 重绘幅度 | simple | - | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，13 个样本，一致性 77%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 16，13 个样本
- 采样算法 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，13 个样本，一致性 69%
- 重绘幅度 最常用 simple，13 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 16，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
