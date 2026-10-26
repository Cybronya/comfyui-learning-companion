---
name: unknown_workflow_video_lora_sampler_197
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.932
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/反推提示词/13ttv4s_2048991888820150273.json, 图片生成/文生图/Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1978391537375662082.json, 视频生成/文生视频/(官方版10+4)Wan2.2 HoloCine电影多镜头分镜实验版V1（目前效果一般）_1982413564600295425.json, 视频生成/文生视频/(官方版10+6)Wan2.2+Palingenesis差异加速高动态720P文生视频（慢速版）v2_1972348168056860674.json, 视频生成/文生视频/(官方版10+6)Wan2.2差异加速高动态720P文生视频v2（慢速版）_1972269268110864386.json, 视频生成/文生视频/(官方版2+2)Wan2.2新版Lighting0928-720P文生视频（极速版）V3_1972287084159496194.json, 视频生成/文生视频/HoloCine模型+ComfyUI，轻松生成多镜头AI电影_1983436800045817857.json, 视频生成/文生视频/HoloCine电影分镜视频模型【Comfy版】_1984101340337078273.json, 视频生成/文生视频/Wan 2.2 lighning V2高低噪文生视频V1_1987455645072953345.json, 视频生成/文生视频/wan2.2官方优化版250928（添加最新4步加速lora）_1973561137847472129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_197

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/反推提示词/13ttv4s_2048991888820150273.json、图片生成/文生图/Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1978391537375662082.json、视频生成/文生视频/(官方版10+4)Wan2.2 HoloCine电影多镜头分镜实验版V1（目前效果一般）_1982413564600295425.json、视频生成/文生视频/(官方版10+6)Wan2.2+Palingenesis差异加速高动态720P文生视频（慢速版）v2_1972348168056860674.json、视频生成/文生视频/(官方版10+6)Wan2.2差异加速高动态720P文生视频v2（慢速版）_1972269268110864386.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 9/10 个有
- `ImageFromBatch+` —— 9/10 个有
- `ImageSharpen` —— 8/10 个有
- `JWInteger` —— 8/10 个有
- `TorchCompileModel` —— 8/10 个有
- `easy cleanGpuUsed` —— 8/10 个有
- `Text Multiline` —— 7/10 个有
- `DownloadAndLoadGIMMVFIModel` —— 6/10 个有
- `GIMMVFI_interpolate` —— 6/10 个有
- `Label (rgthree)` —— 2/10 个有
- `CreateVideo` —— 1/10 个有
- `LayerUtility: PurgeVRAM` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `PreViewVideo` —— 1/10 个有
- `RTXVideoSuperResolution` —— 1/10 个有
- `WanContextWindowsManual` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 10 | 100% |
| Prompt 约束强度(CFG) | 10 | 8 - 10 | 10 | 94% |
| 采样算法 | 1 | 1 - 4 | 10 | 35% |
| 调度器 | uni_pc | - | 10 | 50% |
| 重绘幅度 | simple | - | 10 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，10 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 8 - 10，10 个样本，取值集中（一致性 94%）
- 采样算法 中位数 1，观测区间 1 - 4，10 个样本，取值分散，一致性仅 35%
- 调度器 最常用 uni_pc，10 个样本，一致性 50%
- 重绘幅度 最常用 simple，10 个样本，一致性 90%
