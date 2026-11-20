---
name: unknown_workflow_video_sampler_clip_86
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.964625
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJv2, ImageScaleBy, ImpactInt, KSamplerAdvanced, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveStringMultiline, RIFE VFI, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2 Remix-高动态电影质感模型 图生视频_1988090119234236418.json, 视频生成/图生视频/视频全能融合模型Smooth Mix wan2.2_1979453083128336385.json, 视频生成/图生视频/视频生成-生成视频片段_2010181863981191170.json, 视频生成/图生视频/视频生成-生成视频片段_2012343495582818305.json, 视频生成/图生视频/首尾帧图生视频Wan2.2-Smooth Mix 超丝滑动态电影感画质极速渲染 工作流_1981312323858104321.json, 视频生成/图生视频/首尾帧视频_1986671035942662146.json, 视频生成/图生视频/高动态电影级首尾帧Wan2.2-Smooth Mix 超丝滑动态1.0_1986030132559314946.json, 视频生成/图生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 首尾帧视频🚵_1979384908328112130.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_86

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/wan2.2 Remix-高动态电影质感模型 图生视频_1988090119234236418.json、视频生成/图生视频/视频全能融合模型Smooth Mix wan2.2_1979453083128336385.json、视频生成/图生视频/视频生成-生成视频片段_2010181863981191170.json、视频生成/图生视频/视频生成-生成视频片段_2012343495582818305.json、视频生成/图生视频/首尾帧图生视频Wan2.2-Smooth Mix 超丝滑动态电影感画质极速渲染 工作流_1981312323858104321.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `ImpactInt`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `RIFE VFI`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Fast Bypasser (rgthree)` —— 7/8 个有
- `Mute / Bypass Repeater (rgthree)` —— 7/8 个有
- `Seed (rgthree)` —— 7/8 个有
- `wanBlockSwap` —— 6/8 个有
- `WanFirstLastFrameToVideo` —— 5/8 个有
- `WanImageToVideo` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `AILab_QwenVL` —— 1/8 个有
- `GetImageSize+` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `PurgeVRAM_UTK` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `TextCombinerTwo` —— 1/8 个有
- `easy imageScaleDownToSize` —— 1/8 个有
- `easy showAnything` —— 1/8 个有
- `ttN text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler_ancestral | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
