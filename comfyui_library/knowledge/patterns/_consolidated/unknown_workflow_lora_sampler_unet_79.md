---
name: unknown_workflow_lora_sampler_unet_79
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.681222
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3SigmaShift, ModelAttentionBackend, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy int]
problems: []
missing: []
members: [图片生成/图生图/海螺H3标准工作流-01-首尾帧生视频_2093944374529974273.json, 图片生成/图生图/海螺H3标准工作流-02-单图生视频_2093940538071412737.json, 图片生成/图生图/海螺H3标准工作流-03-人物参考跳舞_2093911326912503810.json, 视频生成/图生视频/海螺H3视频编辑-人物替换(效果不稳定)_2095974697245691905.json, 视频生成/图生视频/海螺H3视频编辑-人物替换V1_2094669610908995586.json, 视频生成/图生视频/海螺H3视频编辑-人物替换V1_2098982875499687938.json, 视频生成/图生视频/海螺H3视频编辑-人物替换V1_2100156710735405057.json, 视频生成/文生视频/MinimaxH3+音频驱动多参_2092941359513694209.json, 视频生成/文生视频/海螺H3视频编辑-人物替换V3-强化替换效果_2092546456971464705.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_79

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/海螺H3标准工作流-01-首尾帧生视频_2093944374529974273.json、图片生成/图生图/海螺H3标准工作流-02-单图生视频_2093940538071412737.json、图片生成/图生图/海螺H3标准工作流-03-人物参考跳舞_2093911326912503810.json、视频生成/图生视频/海螺H3视频编辑-人物替换(效果不稳定)_2095974697245691905.json、视频生成/图生视频/海螺H3视频编辑-人物替换V1_2094669610908995586.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 8/9 个有
- `VAEDecodeAudio` —— 8/9 个有
- `MiniMaxH3ReferenceToVideo` —— 7/9 个有
- `VHS_LoadVideo` —— 7/9 个有
- `GetNode` —— 6/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/9 个有
- `PlaySound|pysssss` —— 6/9 个有
- `ResolutionSelector` —— 6/9 个有
- `SetNode` —— 6/9 个有
- `VHS_VideoCombine` —— 6/9 个有
- `VHS_VideoInfo` —— 6/9 个有
- `Bookmark (rgthree)` —— 5/9 个有
- `Label (rgthree)` —— 5/9 个有
- `ComfyMathExpression` —— 4/9 个有
- `PrimitiveFloat` —— 4/9 个有
- `EmptyImage` —— 2/9 个有
- `MiniMaxH3ImageToVideo` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `SaveImage` —— 2/9 个有
- `Int` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `SoundFlow_GetLength` —— 1/9 个有
- `TrimAudioDuration` —— 1/9 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
