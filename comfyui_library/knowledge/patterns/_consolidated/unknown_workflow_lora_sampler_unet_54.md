---
name: unknown_workflow_lora_sampler_unet_54
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7026
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/全能参考视频_Minimax H3_v2_2107298598168915969.json, 图片生成/图生图/海螺H3标准工作流-01-首尾帧生视频_2093944374529974273.json, 图片生成/图生图/海螺H3标准工作流-02-单图生视频_2093940538071412737.json, 图片生成/图生图/海螺H3标准工作流-03-人物参考跳舞_2093911326912503810.json, 视频生成/图生视频/海螺H3视频编辑-人物替换(效果不稳定)_2095974697245691905.json, 视频生成/图生视频/海螺H3视频编辑-人物替换V1_2094669610908995586.json, 视频生成/图生视频/海螺H3视频编辑-人物替换V1_2098982875499687938.json, 视频生成/图生视频/海螺H3视频编辑-人物替换V1_2100156710735405057.json, 视频生成/文生视频/MinimaxH3+音频驱动多参_2092941359513694209.json, 视频生成/文生视频/海螺H3视频编辑-人物替换V3-强化替换效果_2092546456971464705.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_54

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/全能参考视频_Minimax H3_v2_2107298598168915969.json、图片生成/图生图/海螺H3标准工作流-01-首尾帧生视频_2093944374529974273.json、图片生成/图生图/海螺H3标准工作流-02-单图生视频_2093940538071412737.json、图片生成/图生图/海螺H3标准工作流-03-人物参考跳舞_2093911326912503810.json、视频生成/图生视频/海螺H3视频编辑-人物替换(效果不稳定)_2095974697245691905.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 9/10 个有
- `MiniMaxH3SigmaShift` —— 9/10 个有
- `ModelAttentionBackend` —— 9/10 个有
- `PrimitiveInt` —— 9/10 个有
- `VAEDecodeAudio` —— 9/10 个有
- `easy anythingIndexSwitch` —— 9/10 个有
- `easy int` —— 9/10 个有
- `GetImageSizeAndCount` —— 8/10 个有
- `MiniMaxH3ReferenceToVideo` —— 8/10 个有
- `VHS_LoadVideo` —— 7/10 个有
- `GetNode` —— 6/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/10 个有
- `PlaySound|pysssss` —— 6/10 个有
- `ResolutionSelector` —— 6/10 个有
- `SetNode` —— 6/10 个有
- `VHS_VideoCombine` —— 6/10 个有
- `VHS_VideoInfo` —— 6/10 个有
- `Bookmark (rgthree)` —— 5/10 个有
- `ComfyMathExpression` —— 5/10 个有
- `Label (rgthree)` —— 5/10 个有
- `PrimitiveFloat` —— 5/10 个有
- `EmptyImage` —— 2/10 个有
- `MiniMaxH3ImageToVideo` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `SaveImage` —— 2/10 个有
- `Int` —— 1/10 个有
- `LoadAudio` —— 1/10 个有
- `SoundFlow_GetLength` —— 1/10 个有
- `TrimAudioDuration` —— 1/10 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
