---
name: unknown_workflow_lora_sampler_unet_14
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.902222
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, MiniMaxH3TurboLoRA, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, SpectrumApplyMiniMaxH3, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Minimax H3 文生图工作流（带放大、提示词模版）_2090801005020672001.json, 视频生成/图生视频/Minima H3 多图参考生视频工作流（极速15秒1080P）_2090769195763068930.json, 视频生成/图生视频/Minimax H3 AI萌宠视频工作流（宠物带货15秒1080P）_2096442093140008962.json, 视频生成/图生视频/Minimax H3 单图参考AI图生视频工作流（极速10秒1080P）_2098632894154633217.json, 视频生成/图生视频/Minimax H3 单图参考AI图生视频工作流（极速10秒1080P）_2102648250376482817.json, 视频生成/图生视频/Minimax H3 单图生视频工作流加速版_2106591527647662081.json, 视频生成/图生视频/Minimax H3 单图生视频工作流（极速15秒1080P）_2090716594468118530.json, 视频生成/图生视频/Minimax H3 唱歌对口型数字人工作流（含提示词模版）_2090749193135681538.json, 视频生成/图生视频/Minimax H3 唱歌对口型数字人工作流（含提示词模版）_2101259585813311489.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_14

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Minimax H3 文生图工作流（带放大、提示词模版）_2090801005020672001.json、视频生成/图生视频/Minima H3 多图参考生视频工作流（极速15秒1080P）_2090769195763068930.json、视频生成/图生视频/Minimax H3 AI萌宠视频工作流（宠物带货15秒1080P）_2096442093140008962.json、视频生成/图生视频/Minimax H3 单图参考AI图生视频工作流（极速10秒1080P）_2098632894154633217.json、视频生成/图生视频/Minimax H3 单图参考AI图生视频工作流（极速10秒1080P）_2102648250376482817.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
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
- `SpectrumApplyMiniMaxH3`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 8/9 个有
- `LoadImage` —— 8/9 个有
- `SaveVideo` —— 8/9 个有
- `ExtendIntermediateSigmas` —— 3/9 个有
- `LoadAudio` —— 2/9 个有
- `LoadVideo` —— 2/9 个有
- `GetImagesFromBatchIndexed` —— 1/9 个有
- `ImageUpscaleWithModel` —— 1/9 个有
- `PreviewAudio` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `PrimitiveFloat` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `UpscaleModelLoader` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
