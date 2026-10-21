---
name: unknown_workflow_video_lora_sampler_279
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.5925
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/动态壁纸生成-Minimax_h3_2095801933113155586.json, 视频生成/图生视频/海螺H3视频编辑-人物替换(效果不稳定)_2095974697245691905.json, 视频生成/图生视频/海螺H3视频编辑-人物替换V1_2094669610908995586.json, 视频生成/图生视频/海螺H3视频编辑-人物替换V1_2098982875499687938.json, 视频生成/图生视频/海螺H3视频编辑-人物替换V1_2100156710735405057.json, 视频生成/图生视频/海螺H3视频编辑-人物替换V3-强化替换效果_2092546456971464705.json, 视频生成/文生视频/MinimaxH3+音频驱动多参_2092941359513694209.json, 视频生成/文生视频/海螺H3视频编辑-人物替换V3-强化替换效果_2092546456971464705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_279

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/动态壁纸生成-Minimax_h3_2095801933113155586.json、视频生成/图生视频/海螺H3视频编辑-人物替换(效果不稳定)_2095974697245691905.json、视频生成/图生视频/海螺H3视频编辑-人物替换V1_2094669610908995586.json、视频生成/图生视频/海螺H3视频编辑-人物替换V1_2098982875499687938.json、视频生成/图生视频/海螺H3视频编辑-人物替换V1_2100156710735405057.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 7/8 个有
- `PlaySound|pysssss` —— 7/8 个有
- `PrimitiveInt` —— 7/8 个有
- `PrimitiveStringMultiline` —— 7/8 个有
- `SaveVideo` —— 7/8 个有
- `VHS_VideoInfo` —— 7/8 个有
- `easy anythingIndexSwitch` —— 7/8 个有
- `easy int` —— 7/8 个有
- `Bookmark (rgthree)` —— 6/8 个有
- `GetImageSizeAndCount` —— 6/8 个有
- `Label (rgthree)` —— 6/8 个有
- `EmptyImage` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `ComfyMathExpression` —— 1/8 个有
- `Int` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `LoadAudio` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `MiniMaxH3PromptEnhancerT8` —— 1/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `SoundFlow_GetLength` —— 1/8 个有
- `T8LLMProviderConfig` —— 1/8 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
