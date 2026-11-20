---
name: unknown_workflow_video_sampler_clip_137
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.4886
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, GetNode, JoinStrings, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, Qwen3_VQA, RIFE VFI, SetNode, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/【洋洋】-DasiwaV9图生视频自动提示词_2017055688299651074.json, 视频生成/图生视频/漫剧-DasiwaV9单图生视频（高动效）_2008405529701388289.json, 视频生成/图生视频/漫剧-DasiwaV9单图生视频（高动效）_2050908544660197378.json, 视频生成/图生视频/漫剧-三图首中尾帧DasiwaV9 图生视频（高动效）_2013245533510438913.json, 视频生成/图生视频/漫剧-双图首尾帧DasiwaV9 图生视频（高动效）_2013236610988515330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_137

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/【洋洋】-DasiwaV9图生视频自动提示词_2017055688299651074.json、视频生成/图生视频/漫剧-DasiwaV9单图生视频（高动效）_2008405529701388289.json、视频生成/图生视频/漫剧-DasiwaV9单图生视频（高动效）_2050908544660197378.json、视频生成/图生视频/漫剧-三图首中尾帧DasiwaV9 图生视频（高动效）_2013245533510438913.json、视频生成/图生视频/漫剧-双图首尾帧DasiwaV9 图生视频（高动效）_2013236610988515330.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `GetNode`
- `JoinStrings`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `Qwen3_VQA`
- `RIFE VFI`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Int` —— 4/5 个有
- `Text` —— 4/5 个有
- `CLIPVisionEncode` —— 3/5 个有
- `PainterI2V` —— 3/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `INTConstant` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `WanFirstLastFrameToVideo` —— 1/5 个有
- `WanFirstMiddleLastFrameToVideo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
