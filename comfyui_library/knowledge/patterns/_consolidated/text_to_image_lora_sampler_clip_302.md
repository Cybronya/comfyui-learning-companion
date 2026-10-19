---
name: text_to_image_lora_sampler_clip_302
type: Text To Image
frequency: 2
level: weak
coverage: 0.841
common_nodes: [AILab_ImageStitch, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CM_IntToFloat, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, JoinStrings, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RHHiddenNodes, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy int, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3动作迁移 参考视频动作迁移角色一致性生成_2099923089667747842.json, 视频生成/图生视频/MINIMAX-H3动作迁移-角色一致性图生视频工作流_2087345943531311106.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_302

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/H3动作迁移 参考视频动作迁移角色一致性生成_2099923089667747842.json、视频生成/图生视频/MINIMAX-H3动作迁移-角色一致性图生视频工作流_2087345943531311106.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_ImageStitch`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `JoinStrings`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy int`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `GetVideoComponents` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `ShellAgentPluginOutputText` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
