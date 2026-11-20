---
name: unknown_workflow_video_lora_sampler_313
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.642556
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/Minimax_人物替换_2094693215466250241.json, 数字人/数字人/MinimaxH3 角色替换_2092994502658183169.json, 视频生成/图生视频/动态壁纸生成-Minimax_h3_2095801933113155586.json, 视频生成/图生视频/动态壁纸生成-Minimax_h3_2116665021953568769.json, 视频生成/图生视频/海螺H3视频编辑-人物替换(效果不稳定)_2095974697245691905.json, 视频生成/图生视频/海螺H3视频编辑-人物替换V1_2094669610908995586.json, 视频生成/图生视频/海螺H3视频编辑-人物替换V1_2098982875499687938.json, 视频生成/图生视频/海螺H3视频编辑-人物替换V1_2100156710735405057.json, 视频生成/文生视频/海螺H3视频编辑-人物替换V3-强化替换效果_2092546456971464705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_313

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/Minimax_人物替换_2094693215466250241.json、数字人/数字人/MinimaxH3 角色替换_2092994502658183169.json、视频生成/图生视频/动态壁纸生成-Minimax_h3_2095801933113155586.json、视频生成/图生视频/动态壁纸生成-Minimax_h3_2116665021953568769.json、视频生成/图生视频/海螺H3视频编辑-人物替换(效果不稳定)_2095974697245691905.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `VAEDecodeAudio` —— 8/9 个有
- `CreateVideo` —— 7/9 个有
- `GetImageSizeAndCount` —— 7/9 个有
- `ImageResizeKJv2` —— 7/9 个有
- `ResolutionSelector` —— 7/9 个有
- `VHS_VideoInfo` —— 7/9 个有
- `PrimitiveStringMultiline` —— 6/9 个有
- `easy int` —— 6/9 个有
- `PlaySound|pysssss` —— 5/9 个有
- `PrimitiveInt` —— 5/9 个有
- `SaveVideo` —— 5/9 个有
- `easy anythingIndexSwitch` —— 5/9 个有
- `Bookmark (rgthree)` —— 4/9 个有
- `Label (rgthree)` —— 4/9 个有
- `Int` —— 3/9 个有
- `JjkText` —— 3/9 个有
- `MathExpression|pysssss` —— 3/9 个有
- `EmptyImage` —— 2/9 个有
- `MiniMaxH3PromptEnhancerT8` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `T8LLMProviderConfig` —— 2/9 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/9 个有
- `VideoCombineV2` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
