---
name: unknown_workflow_video_sampler_clip_47
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.967273
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJv2, ImpactInt, KSamplerAdvanced, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveStringMultiline, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/1988090119234236418.json, 视频生成/图生视频/1980432616040148994.json, 视频生成/图生视频/1983880606536925186.json, 视频生成/图生视频/2010998394537381889.json, 视频生成/图生视频/2035897809894903809.json, 视频生成/图生视频/2039617670403858433.json, 视频生成/图生视频/2041028074229211137.json, 视频生成/图生视频/1980633692215361538.json, 视频生成/图生视频/2006925723407228930.json, 视频生成/图生视频/2009598515076407298.json, 视频生成/图生视频/1979453083128336385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/1988090119234236418.json、视频生成/图生视频/1980432616040148994.json、视频生成/图生视频/1983880606536925186.json、视频生成/图生视频/2010998394537381889.json、视频生成/图生视频/2035897809894903809.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `ImpactInt`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Fast Bypasser (rgthree)` —— 10/11 个有
- `ImageScaleBy` —— 10/11 个有
- `Mute / Bypass Repeater (rgthree)` —— 10/11 个有
- `RIFE VFI` —— 10/11 个有
- `Seed (rgthree)` —— 10/11 个有
- `WanImageToVideo` —— 10/11 个有
- `wanBlockSwap` —— 10/11 个有
- `Fast Groups Bypasser (rgthree)` —— 2/11 个有
- `WanFirstLastFrameToVideo` —— 2/11 个有
- `easy showAnything` —— 2/11 个有
- `AILab_QwenVL` —— 1/11 个有
- `CR Text Concatenate` —— 1/11 个有
- `GetImageSize+` —— 1/11 个有
- `ImageBatchGet` —— 1/11 个有
- `LoadAudio` —— 1/11 个有
- `LoraLoaderModelOnly` —— 1/11 个有
- `PurgeVRAM_UTK` —— 1/11 个有
- `RHHiddenNodes` —— 1/11 个有
- `TextCombinerTwo` —— 1/11 个有
- `easy imageScaleDownToSize` —— 1/11 个有
- `easy imageSplitGrid` —— 1/11 个有
- `ttN text` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 91% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 11 | 91% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | euler_ancestral | - | 11 | 91% |
| 重绘幅度 | simple | - | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 91%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，11 个样本，取值集中（一致性 91%）
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，11 个样本，一致性 91%
- 重绘幅度 最常用 simple，11 个样本，一致性 100%
