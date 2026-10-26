---
name: unknown_workflow_lora_sampler_unet_27
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.902563
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, MiniMaxH3TurboLoRA, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/AI视频模型转图像编辑_2089665130316525570.json, 图片生成/图生图/Minimax H3 图像编辑工作流（支持多图、带放大）_2091499168857681922.json, 图片生成/图生图/Minimax_H3_图像编辑写实工作流支持多图、带放大_2096876812314959874.json, 图片生成/图生图/Minimax_H3_图像编辑写实工作流支持多图、带放大_2097171139620589569.json, 图片生成/图生图/Minimax_H3_图像编辑工作流支持多图、带放大_2093245449938489345.json, 图片生成/图生图/Minimax_H3_图像编辑工作流支持多图、带放大_2093517263633731585.json, 图片生成/文生图/Minimax H3 文生图工作流（带放大、提示词模版）_2090801005020672001.json, 视频生成/图生视频/Minima H3 多图参考生视频工作流（极速15秒1080P）_2090769195763068930.json, 视频生成/图生视频/Minimax H3 AI萌宠视频工作流（宠物带货15秒1080P）_2096442093140008962.json, 视频生成/图生视频/Minimax H3 单图参考AI图生视频工作流（极速10秒1080P）_2098632894154633217.json, 视频生成/图生视频/Minimax H3 单图参考AI图生视频工作流（极速10秒1080P）_2102648250376482817.json, 视频生成/图生视频/Minimax H3 单图生视频工作流加速版_2106591527647662081.json, 视频生成/图生视频/Minimax H3 单图生视频工作流（极速15秒1080P）_2090716594468118530.json, 视频生成/图生视频/Minimax H3 唱歌对口型数字人工作流（含提示词模版）_2090749193135681538.json, 视频生成/图生视频/Minimax H3 唱歌对口型数字人工作流（含提示词模版）_2101259585813311489.json, 视频生成/图生视频/Minimax H3 模仿跳舞工作流（动作迁移、舞蹈模仿、自动生成提示词）_2102956330800734209.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_27

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/AI视频模型转图像编辑_2089665130316525570.json、图片生成/图生图/Minimax H3 图像编辑工作流（支持多图、带放大）_2091499168857681922.json、图片生成/图生图/Minimax_H3_图像编辑写实工作流支持多图、带放大_2096876812314959874.json、图片生成/图生图/Minimax_H3_图像编辑写实工作流支持多图、带放大_2097171139620589569.json、图片生成/图生图/Minimax_H3_图像编辑工作流支持多图、带放大_2093245449938489345.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyModelAdapter`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3TurboLoRA`
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 15/16 个有
- `SpectrumApplyMiniMaxH3` —— 15/16 个有
- `CreateVideo` —— 10/16 个有
- `SaveVideo` —— 9/16 个有
- `GetImagesFromBatchIndexed` —— 7/16 个有
- `ImageUpscaleWithModel` —— 7/16 个有
- `PreviewImage` —— 7/16 个有
- `SaveImage` —— 7/16 个有
- `UpscaleModelLoader` —— 7/16 个有
- `PreviewAudio` —— 6/16 个有
- `Image Comparer (rgthree)` —— 5/16 个有
- `ExtendIntermediateSigmas` —— 4/16 个有
- `LoadVideo` —— 3/16 个有
- `LoadAudio` —— 2/16 个有
- `PDGeminiAPIKey` —— 1/16 个有
- `PreviewTextNode` —— 1/16 个有
- `PrimitiveFloat` —— 1/16 个有
- `PrimitiveInt` —— 1/16 个有
- `PrimitiveStringMultiline` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
