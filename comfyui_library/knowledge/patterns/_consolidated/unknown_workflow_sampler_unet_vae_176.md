---
name: unknown_workflow_sampler_unet_vae_176
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.694
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 文生视频 _ 图生视频  首尾帧_1934647540794990594.json, 视频生成/文生视频/MiniMax H3 文生视频-comfyui版_2084188214616739841.json, 视频生成/文生视频/MiniMax H3图生视频（支持文生视频，首_尾帧生成）_2084161667742654466.json, 视频生成/文生视频/MiniMax-H3 图生视频 5秒视频只需3分钟+全节点注释_2084508809128669186.json, 视频生成/文生视频/MiniMax-H3_插帧图生视频_2084843609874067458.json, 视频生成/文生视频/MiniMax-H3首尾帧生视频 5秒视频只需要3分钟+全节点注释_2084503505364148226.json, 视频生成/文生视频/h3文生_首尾帧视频_2084566244484804610.json, 视频生成/文生视频/文生视频_图生视频MiniMax+H3_2084798105811251201.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_176

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 文生视频 _ 图生视频  首尾帧_1934647540794990594.json、视频生成/文生视频/MiniMax H3 文生视频-comfyui版_2084188214616739841.json、视频生成/文生视频/MiniMax H3图生视频（支持文生视频，首_尾帧生成）_2084161667742654466.json、视频生成/文生视频/MiniMax-H3 图生视频 5秒视频只需3分钟+全节点注释_2084508809128669186.json、视频生成/文生视频/MiniMax-H3_插帧图生视频_2084843609874067458.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 6/8 个有
- `ResolutionSelector` —— 5/8 个有
- `CR Text` —— 4/8 个有
- `easy showAnything` —— 4/8 个有
- `VHS_VideoCombine` —— 3/8 个有
- `孤海注释` —— 3/8 个有
- `忽略多组孤海` —— 3/8 个有
- `GoohaiUniversalSlider` —— 2/8 个有
- `JjkText` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `孤海图像缩放按像素` —— 2/8 个有
- `GetImageSize+` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `RIFE VFI` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
