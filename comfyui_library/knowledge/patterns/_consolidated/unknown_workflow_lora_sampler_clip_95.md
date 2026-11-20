---
name: unknown_workflow_lora_sampler_clip_95
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.530571
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, GetNode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SaveVideo, SetNode, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, WanVaceToVideo]
problems: []
missing: []
members: [平台全量/video_wan2_2_14B_t2v_vace_视频到视频_1950470565654126593.json, 视频生成/图生视频/video_wan2_2_14B_t2v_vace_主体参考_1950134671634030593.json, 视频生成/图生视频/video_wan2_2_14B_t2v_vace_主体参考_1950440194634858497.json, 视频生成/图生视频/video_wan2_2_14B_t2v_vace_视频到视频_1950138726648299522.json, 视频生成/图生视频/video_wan2_2_14B_t2v_vace_首尾帧控制_1950138479567134721.json, 视频生成/图生视频/video_wan2_2_14B_vace_图生视频_1950130788953145346.json, 视频生成/图生视频/video_wan2_2_14B_vace_图生视频_1950436641396670465.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_95

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/video_wan2_2_14B_t2v_vace_视频到视频_1950470565654126593.json、视频生成/图生视频/video_wan2_2_14B_t2v_vace_主体参考_1950134671634030593.json、视频生成/图生视频/video_wan2_2_14B_t2v_vace_主体参考_1950440194634858497.json、视频生成/图生视频/video_wan2_2_14B_t2v_vace_视频到视频_1950138726648299522.json、视频生成/图生视频/video_wan2_2_14B_t2v_vace_首尾帧控制_1950138479567134721.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：53%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveVideo`
- `SetNode`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 5/7 个有
- `AILab_ColorInput` —— 3/7 个有
- `DepthAnythingPreprocessor` —— 2/7 个有
- `RMBG` —— 2/7 个有
- `VHS_LoadVideo` —— 2/7 个有
- `WanVideoVACEStartToEndFrame` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | lcm | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
