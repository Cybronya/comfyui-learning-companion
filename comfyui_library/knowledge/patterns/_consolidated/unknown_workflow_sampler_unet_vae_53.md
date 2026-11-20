---
name: unknown_workflow_sampler_unet_vae_53
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.806857
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Minimax_文生视频_8步加速_2077975666892558338.json, 视频生成/文生视频/Minimax文生视频高质量极速版_2084997026189758466.json, 视频生成/文生视频/Minimxa-lightx2v-SLA加速文生图_2091334717189746689.json, 视频生成/文生视频/VividMuse_MiniMax_H3_文生视频_2084269402014437378.json, 视频生成/文生视频/comfyui官方工作流-video_minimax_h3_t2v_2084148000615657474.json, 视频生成/文生视频/minimax_h3 4steps加速_2085757759953399809.json, 视频生成/文生视频/minimax_h3_lightx2v正式版 文生、图生、首尾帧加速_2085755880041181185.json, 视频生成/文生视频/minimax_h3_文生视频_2084110685591654402.json, 视频生成/文生视频/minimax_h3_文生视频_8步加速_2084159928788410370.json, 视频生成/文生视频/minimax文字出视频_2084271438885904386.json, 视频生成/文生视频/【Gensor-AI】MINIMAX-H3工作流合集【加速版】_2085550246054162433.json, 视频生成/文生视频/【V-zion】Minimax-H3【文生视频_首尾帧_首帧_尾帧】附加提示词模板_2084613485291462658.json, 视频生成/文生视频/开源版MINIMAX-H3 文生视频 图生视频 多图参考生视频 三大工作流合集_2084584790304583681.json, 视频生成/文生视频/开源版MINIMAX-H3 文生视频 图生视频 多图参考生视频 三大工作流合集_2084619362476052481.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_53

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/文生视频/Minimax_文生视频_8步加速_2077975666892558338.json、视频生成/文生视频/Minimax文生视频高质量极速版_2084997026189758466.json、视频生成/文生视频/Minimxa-lightx2v-SLA加速文生图_2091334717189746689.json、视频生成/文生视频/VividMuse_MiniMax_H3_文生视频_2084269402014437378.json、视频生成/文生视频/comfyui官方工作流-video_minimax_h3_t2v_2084148000615657474.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 12/14 个有
- `SaveVideo` —— 12/14 个有
- `MiniMaxH3ImageToVideo` —— 11/14 个有
- `PrimitiveStringMultiline` —— 7/14 个有
- `JjkText` —— 6/14 个有
- `LoadImage` —— 6/14 个有
- `LoraLoaderModelOnly` —— 6/14 个有
- `Fast Groups Bypasser (rgthree)` —— 4/14 个有
- `LoadAudio` —— 4/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/14 个有
- `MiniMaxH3ReferenceToVideo` —— 4/14 个有
- `PathchSageAttentionKJ` —— 3/14 个有
- `VHS_VideoCombine` —— 2/14 个有
- `CR Prompt Text` —— 1/14 个有
- `DF_Float` —— 1/14 个有
- `EasyCache` —— 1/14 个有
- `MiniMaxH3BlockCacheT8` —— 1/14 个有
- `ModelAttentionBackend` —— 1/14 个有
- `Seed (rgthree)` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
