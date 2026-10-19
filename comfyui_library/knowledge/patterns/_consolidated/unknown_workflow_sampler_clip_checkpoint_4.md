---
name: unknown_workflow_sampler_clip_checkpoint_4
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.99225
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, KSamplerSelect, LTXVConditioning, LTXVImgToVideo, LTXVPreprocess, LTXVScheduler, LoadImage, SamplerCustom, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/2061352248059453441.json, 视频生成/图生视频/1922115762343854081.json, 视频生成/图生视频/1922122988903399425.json, 视频生成/图生视频/1920704880137142273.json, 视频生成/图生视频/1920714358920249345.json, 视频生成/图生视频/1922236648937996290.json, 视频生成/图生视频/1948228738078126081.json, 视频生成/图生视频/1947951942166294530.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_4

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2061352248059453441.json、视频生成/图生视频/1922115762343854081.json、视频生成/图生视频/1922122988903399425.json、视频生成/图生视频/1920704880137142273.json、视频生成/图生视频/1920714358920249345.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSamplerSelect`
- `LTXVConditioning`
- `LTXVImgToVideo`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LoadImage`
- `SamplerCustom`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 7/8 个有
- `Int` —— 7/8 个有
- `VHS_VideoCombine` —— 7/8 个有
- `Florence2` —— 2/8 个有
- `LayerMask: LoadFlorence2Model` —— 2/8 个有
- `ImageUpscaleWithModel` —— 1/8 个有
- `Primitive integer [Crystools]` —— 1/8 个有
- `RIFE VFI` —— 1/8 个有
- `SaveAnimatedWEBP` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `SaveWEBM` —— 1/8 个有
- `UpscaleModelLoader` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
