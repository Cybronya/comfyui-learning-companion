---
name: unknown_workflow_video_sampler_unet_10
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.895875
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/minimaxH3全参双人对话test_2084712710343839746.json, 视频生成/图生视频/minimaxH3参考图生成视频_2088465091976056833.json, 视频生成/图生视频/minimaxH3可爱的小兔子_2090680892384694273.json, 视频生成/图生视频/minimaxH3荷叶上舞蹈女孩_2090678919732228098.json, 视频生成/图生视频/minimaxH3首尾帧_2090676134592733185.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T1_2085350214604513281.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T2_2085358927612563457.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T3_2085391641258582017.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T4_2085391626901475329.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T5_2085411686395236353.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T6_2085444171992748033.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T7_2102928115411542018.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T7_2104380315761471490.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T8_2085676923673464834.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T9_2085718493915336705.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词_2086276081564344321.json, 视频生成/图生视频/minimaxh3多参官方指南自动扩展提示词T1_2085348535347802114.json, 视频生成/图生视频/人物微表情变化_2097294907064012801.json, 视频生成/图生视频/人物表情变化动作_2097300292181258241.json, 视频生成/图生视频/创意广告_2087007696313733122.json, 视频生成/图生视频/图生视频提示词自动填充_2086756092205428737.json, 视频生成/图生视频/图生视频电影质感_2087837157028352001.json, 视频生成/图生视频/最新mimimaxH3漫剧镜头T1_2084662928074174466.json, 视频生成/图生视频/来一杯可乐_2097322293583241217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_10

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/minimaxH3全参双人对话test_2084712710343839746.json、视频生成/图生视频/minimaxH3参考图生成视频_2088465091976056833.json、视频生成/图生视频/minimaxH3可爱的小兔子_2090680892384694273.json、视频生成/图生视频/minimaxH3荷叶上舞蹈女孩_2090678919732228098.json、视频生成/图生视频/minimaxH3首尾帧_2090676134592733185.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 24 个 workflow 都包含：
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
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `RHHiddenNodes` —— 16/24 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 16/24 个有
- `ImageConcatenateMulti_UTK` —— 15/24 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 15/24 个有
- `PreviewImage` —— 15/24 个有
- `ResolutionSelector` —— 15/24 个有
- `easy showAnything` —— 14/24 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/24 个有
- `LoadAudio` —— 8/24 个有
- `MiniMaxH3ImageToVideo` —— 8/24 个有
- `RH_Captioner` —— 7/24 个有
- `TextConcatenate_UTK` —— 7/24 个有
- `MiniMaxH3BlockCacheT8` —— 6/24 个有
- `ImageResizeKJv2` —— 2/24 个有
- `RH_Translator` —— 1/24 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
