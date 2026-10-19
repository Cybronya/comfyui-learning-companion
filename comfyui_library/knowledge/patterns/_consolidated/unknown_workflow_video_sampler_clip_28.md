---
name: unknown_workflow_video_sampler_clip_28
type: Unknown Workflow
frequency: 14
level: weak
coverage: 0.937857
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1988236119332536321.json, 视频生成/图生视频/1951292355926282242.json, 视频生成/图生视频/2038634972579373058.json, 视频生成/图生视频/2018657772811853825.json, 视频生成/图生视频/2018729929084510209.json, 视频生成/图生视频/2036515691074949121.json, 视频生成/图生视频/1979531861057769474.json, 视频生成/图生视频/1986278808032595970.json, 视频生成/图生视频/2007316422707388418.json, 视频生成/图生视频/2010181863981191170.json, 视频生成/图生视频/2012343495582818305.json, 视频生成/图生视频/2006937829007433729.json, 视频生成/图生视频/1979384591175815170.json, 视频生成/图生视频/1979384908328112130.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/1988236119332536321.json、视频生成/图生视频/1951292355926282242.json、视频生成/图生视频/2038634972579373058.json、视频生成/图生视频/2018657772811853825.json、视频生成/图生视频/2018729929084510209.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 13/14 个有
- `CLIPVisionLoader` —— 13/14 个有
- `PathchSageAttentionKJ` —— 13/14 个有
- `ImpactInt` —— 12/14 个有
- `ModelPatchTorchSettings` —— 12/14 个有
- `SimpleMath+` —— 12/14 个有
- `easy cleanGpuUsed` —— 12/14 个有
- `PrimitiveStringMultiline` —— 11/14 个有
- `Seed (rgthree)` —— 11/14 个有
- `WanImageToVideo` —— 11/14 个有
- `Fast Bypasser (rgthree)` —— 7/14 个有
- `Mute / Bypass Repeater (rgthree)` —— 7/14 个有
- `wanBlockSwap` —— 7/14 个有
- `RIFE VFI` —— 6/14 个有
- `ImageScaleBy` —— 5/14 个有
- `GetNode` —— 2/14 个有
- `Note Plus (mtb)` —— 2/14 个有
- `RHHiddenNodes` —— 2/14 个有
- `SetNode` —— 2/14 个有
- `WanAdvancedI2V` —— 2/14 个有
- `LayerUtility: PurgeVRAM V2` —— 1/14 个有
- `PainterI2V` —— 1/14 个有
- `RH_LLMAPI_NODE` —— 1/14 个有
- `ShowText` —— 1/14 个有
- `TextInput_` —— 1/14 个有
- `WanFirstLastFrameToVideo` —— 1/14 个有
- `easy textSwitch` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 14 | 57% |
| Prompt 约束强度(CFG) | 6 | 4 - 20 | 14 | 45% |
| 采样算法 | 1 | 1 - 3.5 | 14 | 45% |
| 调度器 | euler_ancestral | - | 14 | 93% |
| 重绘幅度 | simple | - | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，14 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 20，14 个样本，取值分散，一致性仅 45%
- 采样算法 中位数 1，观测区间 1 - 3.5，14 个样本，取值分散，一致性仅 45%
- 调度器 最常用 euler_ancestral，14 个样本，一致性 93%
- 重绘幅度 最常用 simple，14 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
