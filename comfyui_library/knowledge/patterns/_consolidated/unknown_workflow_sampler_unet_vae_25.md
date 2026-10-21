---
name: unknown_workflow_sampler_unet_vae_25
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.8156
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: [CR Text, 孤海图像缩放按像素, 忽略多组孤海]
members: [视频生成/图生视频/1934647540794990594.json, 视频生成/图生视频/MiniMax-H3-图生视频_2084259365334372354.json, 视频生成/图生视频/MiniMax-H3-图生视频（4步生视频超级加速）_2085221255543877633.json, 视频生成/图生视频/MiniMax-H3-首尾帧视频_2084274212876939265.json, 视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2100206617605267458.json, 视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2100585354809139202.json, 视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2101121504195997698.json, 视频生成/图生视频/Minimax-h3图生视频版_2084511817468039169.json, 视频生成/图生视频/地表最强Minimax-h3图生视频版_2084422222730588162.json, 视频生成/图生视频/地表最强Minimax-h3完美首尾帧版_2084469809009483778.json, 视频生成/文生视频/1934647540794990594.json, 视频生成/文生视频/260817001.MiniMax H3 文生丨图生视频_2089296462692835330.json, 视频生成/文生视频/h3文生_首尾帧视频_2084566244484804610.json, 视频生成/文生视频/地表最强开源视频！Minimax-h3 文生丨图生视频版 26-08-03_2084186070467567618.json, 视频生成/文生视频/文生视频_图生视频MiniMax+H3_2084798105811251201.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_25

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/1934647540794990594.json、视频生成/图生视频/MiniMax-H3-图生视频_2084259365334372354.json、视频生成/图生视频/MiniMax-H3-图生视频（4步生视频超级加速）_2085221255543877633.json、视频生成/图生视频/MiniMax-H3-首尾帧视频_2084274212876939265.json、视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2100206617605267458.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 15 个 workflow 都包含：
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
- `PrimitiveFloat` —— 12/15 个有
- `ResolutionSelector` —— 12/15 个有
- `孤海注释` —— 9/15 个有
- `CR Text` —— 8/15 个有
- `ImageCrop+` —— 5/15 个有
- `ImageScaleToTotalPixels` —— 5/15 个有
- `PathchSageAttentionKJ` —— 4/15 个有
- `PreviewImage` —— 4/15 个有
- `忽略多组孤海` —— 4/15 个有
- `GoohaiUniversalSlider` —— 3/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/15 个有
- `Note Plus (mtb)` —— 3/15 个有
- `easy showAnything` —— 3/15 个有
- `孤海图像缩放按像素` —— 3/15 个有
- `JjkText` —— 2/15 个有
- `EmptyImage` —— 1/15 个有
- `LoraLoaderModelOnly` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、孤海图像缩放按像素、忽略多组孤海
