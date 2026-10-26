---
name: unknown_workflow_video_lora_sampler_311
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.948875
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2_ Motion调整运动速度_2007040869337145346.json, 视频生成/图生视频/Wan2.2_14B_图生视频 (4步加速)_1955097122862350338.json, 视频生成/图生视频/Wan2.2_14B_图生视频 (8步加速)_1966753554679705601.json, 视频生成/图生视频/Wan2.2_图生视频_4步极速版_ComfyUI官方流_2017158021029306369.json, 视频生成/图生视频/Wan2.2_图生视频_4步极速版_ComfyUI官方流_2044039756232790017.json, 视频生成/图生视频/Wan2.2图生视频超级加速_1955793674186604546.json, 视频生成/文生视频/WAN22运动性3xKsampler高速工作流_1959177557772021762.json, 视频生成/文生视频/【老金驿站】提升WAN22运动性3xKsampler高速工作流_1965219730770546689.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_311

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Wan2.2_ Motion调整运动速度_2007040869337145346.json、视频生成/图生视频/Wan2.2_14B_图生视频 (4步加速)_1955097122862350338.json、视频生成/图生视频/Wan2.2_14B_图生视频 (8步加速)_1966753554679705601.json、视频生成/图生视频/Wan2.2_图生视频_4步极速版_ComfyUI官方流_2017158021029306369.json、视频生成/图生视频/Wan2.2_图生视频_4步极速版_ComfyUI官方流_2044039756232790017.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 7/8 个有
- `UNETLoader` —— 6/8 个有
- `PathchSageAttentionKJ` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `LayerUtility: PurgeVRAM V2` —— 3/8 个有
- `PrimitiveFloat` —— 3/8 个有
- `SimpleMath+` —— 3/8 个有
- `UnetLoaderGGUF` —— 3/8 个有
- `PrimitiveInt` —— 2/8 个有
- `easy int` —— 2/8 个有
- `CLIPLoaderGGUF` —— 1/8 个有
- `CR SDXL Aspect Ratio` —— 1/8 个有
- `ImageConcanate` —— 1/8 个有
- `PrimitiveString` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `WanMotionScale` —— 1/8 个有
- `WanVideoVACEStartToEndFrame` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 88% |
| Prompt 约束强度(CFG) | 6.5 | 4 - 8 | 8 | 81% |
| 采样算法 | 1 | 1 - 3.5 | 8 | 37% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 6.5，观测区间 4 - 8，8 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 37%
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
