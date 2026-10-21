---
name: unknown_workflow_video_sampler_vae_15
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.893667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, Text, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/minimaxH3全参双人对话test_2084712710343839746.json, 视频生成/图生视频/minimaxH3参考图生成视频_2088465091976056833.json, 视频生成/图生视频/minimaxH3可爱的小兔子_2090680892384694273.json, 视频生成/图生视频/minimaxH3荷叶上舞蹈女孩_2090678919732228098.json, 视频生成/图生视频/minimaxH3首尾帧_2090676134592733185.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词_2086276081564344321.json, 视频生成/图生视频/minimaxh3吉卜力风格_2086267947819028481.json, 视频生成/图生视频/minimaxh3多参官方指南自动扩展提示词T1_2085348535347802114.json, 视频生成/图生视频/人物微表情变化_2097294907064012801.json, 视频生成/图生视频/人物表情变化动作_2097300292181258241.json, 视频生成/图生视频/人物表情语言变化_2098063808349696001.json, 视频生成/图生视频/双姝_2098043624184434690.json, 视频生成/图生视频/古装美女扮相_2098413882426609665.json, 视频生成/图生视频/快乐的小猫咪_2092480218379411457.json, 视频生成/图生视频/摘松果的松鼠_2091046140023234562.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_15

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/minimaxH3全参双人对话test_2084712710343839746.json、视频生成/图生视频/minimaxH3参考图生成视频_2088465091976056833.json、视频生成/图生视频/minimaxH3可爱的小兔子_2090680892384694273.json、视频生成/图生视频/minimaxH3荷叶上舞蹈女孩_2090678919732228098.json、视频生成/图生视频/minimaxH3首尾帧_2090676134592733185.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Text`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 12/15 个有
- `MiniMaxH3ImageToVideo` —— 11/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/15 个有
- `RH_Captioner` —— 11/15 个有
- `TextConcatenate_UTK` —— 11/15 个有
- `UNETLoader` —— 10/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/15 个有
- `ResolutionSelector` —— 7/15 个有
- `EnhancedLoadDiffusionModel` —— 5/15 个有
- `LoraLoaderBypassModelOnly` —— 5/15 个有
- `MiniMaxH3BlockCacheT8` —— 5/15 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 4/15 个有
- `ImageConcatenateMulti_UTK` —— 3/15 个有
- `LoadAudio` —— 3/15 个有
- `PreviewImage` —— 3/15 个有
- `RHHiddenNodes` —— 3/15 个有
- `ExtractSubstring` —— 2/15 个有
- `ImageResizeKJv2` —— 2/15 个有
- `JWStringToFloat` —— 2/15 个有
- `CreateVideo` —— 1/15 个有
- `ImageFromBatch` —— 1/15 个有
- `LoadVideoUI` —— 1/15 个有
- `ModelAttentionBackend` —— 1/15 个有
- `PD_Extract_Image` —— 1/15 个有
- `SaveVideo` —— 1/15 个有
- `easy indexAnything` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
