---
name: unknown_workflow_sampler_unet_vae_210
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.696143
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [平台全量/MINIMAX H3 跳舞 动作迁移 视频复刻 加速版_2085264637242732546.json, 数字人/数字人/H3.736_1280_2085040704841146370.json, 数字人/数字人/MINIMAX H3-多功能工作流_2084805925134757889.json, 视频生成/图生视频/MINIMAX H3 极速多参工作流_2085299601204137986.json, 视频生成/图生视频/MiniMax+H3+图像+音频参考生视频+lightx2v加速lora_2086827088161628162.json, 视频生成/图生视频/MiniMaxH3+多图参考生视频+提示词反推+加速节点ENG+ENG_2087089620583538690.json, 视频生成/文生视频/MINIMAX H3 极速生成 全能参考图生视频 提示词增强 加速版_2085037354515001345.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_210

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/MINIMAX H3 跳舞 动作迁移 视频复刻 加速版_2085264637242732546.json、数字人/数字人/H3.736_1280_2085040704841146370.json、数字人/数字人/MINIMAX H3-多功能工作流_2084805925134757889.json、视频生成/图生视频/MINIMAX H3 极速多参工作流_2085299601204137986.json、视频生成/图生视频/MiniMax+H3+图像+音频参考生视频+lightx2v加速lora_2086827088161628162.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
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
- `Fast Groups Bypasser (rgthree)` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/7 个有
- `Any Switch (rgthree)` —— 5/7 个有
- `LoadAudio` —— 5/7 个有
- `PreviewAny` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `easy cleanGpuUsed` —— 5/7 个有
- `llama_cpp_instruct_adv` —— 5/7 个有
- `llama_cpp_model_loader` —— 5/7 个有
- `llama_cpp_parameters` —— 5/7 个有
- `CacheDiT_Model_Optimizer` —— 3/7 个有
- `ImpactSwitch` —— 3/7 个有
- `MiniMaxH3SigmaShift` —— 3/7 个有
- `SolAttnPatch` —— 3/7 个有
- `VHS_LoadVideo` —— 3/7 个有
- `GetVideoComponents` —— 2/7 个有
- `JjkText` —— 2/7 个有
- `LoadVideo` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `MiniMaxH3ImageToVideo` —— 2/7 个有
- `PathchSageAttentionKJ` —— 2/7 个有
- `VHS_VideoInfoSource` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
