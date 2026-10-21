---
name: unknown_workflow_video_sampler_clip_59
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.888111
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1988236119332536321.json, 视频生成/图生视频/1951292355926282242.json, 视频生成/图生视频/2038634972579373058.json, 视频生成/图生视频/2018657772811853825.json, 视频生成/图生视频/2018729929084510209.json, 视频生成/图生视频/2036515691074949121.json, 视频生成/图生视频/1979531861057769474.json, 视频生成/图生视频/2050045558773035009.json, 视频生成/图生视频/1979453083128336385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_59

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1988236119332536321.json、视频生成/图生视频/1951292355926282242.json、视频生成/图生视频/2038634972579373058.json、视频生成/图生视频/2018657772811853825.json、视频生成/图生视频/2018729929084510209.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
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
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 8/9 个有
- `CLIPVisionLoader` —— 8/9 个有
- `PathchSageAttentionKJ` —— 8/9 个有
- `ImpactInt` —— 7/9 个有
- `ModelPatchTorchSettings` —— 7/9 个有
- `SimpleMath+` —— 7/9 个有
- `easy cleanGpuUsed` —— 7/9 个有
- `PrimitiveStringMultiline` —— 6/9 个有
- `Seed (rgthree)` —— 6/9 个有
- `GetNode` —— 3/9 个有
- `RIFE VFI` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `ImageScaleBy` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `PainterI2V` —— 1/9 个有
- `RH_LLMAPI_NODE` —— 1/9 个有
- `ShowText` —— 1/9 个有
- `TextInput_` —— 1/9 个有
- `WanFirstLastFrameToVideo` —— 1/9 个有
- `easy textSwitch` —— 1/9 个有
- `wanBlockSwap` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 56% |
| Prompt 约束强度(CFG) | 6 | 4 - 20 | 9 | 37% |
| 采样算法 | 1 | 1 - 3.5 | 9 | 39% |
| 调度器 | euler_ancestral | - | 9 | 89% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 56%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 20，9 个样本，取值分散，一致性仅 37%
- 采样算法 中位数 1，观测区间 1 - 3.5，9 个样本，取值分散，一致性仅 39%
- 调度器 最常用 euler_ancestral，9 个样本，一致性 89%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
