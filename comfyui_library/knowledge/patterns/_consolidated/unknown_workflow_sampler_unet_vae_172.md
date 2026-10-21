---
name: unknown_workflow_sampler_unet_vae_172
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.69875
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PreviewAny, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/MINIMAX H3 极速多参工作流_2085299601204137986.json, 视频生成/图生视频/MiniMax+H3+图像+音频参考生视频+lightx2v加速lora_2086827088161628162.json, 视频生成/图生视频/MiniMaxH3+多图参考生视频+提示词反推+加速节点ENG+ENG_2087089620583538690.json, 视频生成/文生视频/MINIMAX H3 极速生成 全能参考图生视频 提示词增强 加速版_2085037354515001345.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_172

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MINIMAX H3 极速多参工作流_2085299601204137986.json、视频生成/图生视频/MiniMax+H3+图像+音频参考生视频+lightx2v加速lora_2086827088161628162.json、视频生成/图生视频/MiniMaxH3+多图参考生视频+提示词反推+加速节点ENG+ENG_2087089620583538690.json、视频生成/文生视频/MINIMAX H3 极速生成 全能参考图生视频 提示词增强 加速版_2085037354515001345.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PreviewAny`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `Any Switch (rgthree)` —— 2/4 个有
- `CacheDiT_Model_Optimizer` —— 2/4 个有
- `GetVideoComponents` —— 2/4 个有
- `ImpactSwitch` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `LoadVideo` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `MiniMaxH3SigmaShift` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `SolAttnPatch` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
