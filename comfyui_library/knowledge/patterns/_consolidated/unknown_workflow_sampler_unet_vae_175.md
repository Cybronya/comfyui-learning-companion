---
name: unknown_workflow_sampler_unet_vae_175
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.675
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax-h3-数字人视频-图和声音生成视频_2084907676219301889.json, 视频生成/图生视频/minimax_h3_全能参考_2084642306531086337.json, 视频生成/图生视频/多种参考生视频-MiniMax_h3_r2v-视频音频图片参考_2084132425894031361.json, 视频生成/图生视频/开源版Minimax-h3 多模态全能参考版_2084936517058912257.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_175

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Minimax-h3-数字人视频-图和声音生成视频_2084907676219301889.json、视频生成/图生视频/minimax_h3_全能参考_2084642306531086337.json、视频生成/图生视频/多种参考生视频-MiniMax_h3_r2v-视频音频图片参考_2084132425894031361.json、视频生成/图生视频/开源版Minimax-h3 多模态全能参考版_2084936517058912257.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
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
- `AudioCrop` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `PreviewAudio` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `孤海注释` —— 2/4 个有
- `Any To String (mtb)` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ModelPatchTorchSettings` —— 1/4 个有
- `Note Plus (mtb)` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `RH_GetAudioDuration` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `easy anythingIndexSwitch` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有
- `llama_cpp_parameters` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
