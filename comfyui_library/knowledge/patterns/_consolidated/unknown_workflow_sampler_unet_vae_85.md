---
name: unknown_workflow_sampler_unet_vae_85
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.830182
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/H3_海螺_官方-文生API反推_2086103276034027521.json, 视频生成/文生视频/MiniMax H3 FL2VA-文生视频-优化版_2088069601203671041.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-图像 音频参考生视频  DiT int8加速版_2090416308562251777.json, 视频生成/文生视频/MiniMax H3 INT8 W4A8 加速_2086411704518406146.json, 视频生成/文生视频/MiniMax H3 Larry Turbo 加速_2086411713435492353.json, 视频生成/文生视频/MiniMax H3 Larry+attention+cache 满血加速版_2086444236236484609.json, 视频生成/文生视频/MiniMax H3 LightX2V Turbo 加速_2086332815146311681.json, 视频生成/文生视频/MiniMax H3图生视频6倍加速24GB通用版_2086411696771522561.json, 视频生成/文生视频/MiniMax H3图生视频6倍加速48GB高配版_2086411679377743873.json, 视频生成/文生视频/MiniMax H3图生视频6倍加速80GB满配版_2086411651821170689.json, 视频生成/文生视频/MiniMax H3图生视频、首尾帧_2085351688180953090.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_85

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/H3_海螺_官方-文生API反推_2086103276034027521.json、视频生成/文生视频/MiniMax H3 FL2VA-文生视频-优化版_2088069601203671041.json、视频生成/文生视频/MiniMax H3 FL2VA开源版-图像 音频参考生视频  DiT int8加速版_2090416308562251777.json、视频生成/文生视频/MiniMax H3 INT8 W4A8 加速_2086411704518406146.json、视频生成/文生视频/MiniMax H3 Larry Turbo 加速_2086411713435492353.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/11 个有
- `ImageResizeKJv2` —— 7/11 个有
- `PrimitiveStringMultiline` —— 7/11 个有
- `LoraLoaderModelOnly` —— 6/11 个有
- `EasyCache` —— 4/11 个有
- `PathchSageAttentionKJ` —— 4/11 个有
- `CR Text` —— 2/11 个有
- `GetNode` —— 2/11 个有
- `SetNode` —— 2/11 个有
- `ImageCrop+` —— 1/11 个有
- `ImageScaleToTotalPixels` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `RHLLMChatNode` —— 1/11 个有
- `SpectrumApplyMiniMaxH3` —— 1/11 个有
- `StringFunction|pysssss` —— 1/11 个有
- `easy showAnything` —— 1/11 个有
- `workflow>核心` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
