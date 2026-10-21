---
name: text_to_image_lora_sampler_clip_241
type: Text To Image
frequency: 5
level: strong
coverage: 0.8778
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3动作迁移 参考视频动作迁移角色一致性生成_2099923089667747842.json, 视频生成/图生视频/MINIMAX-H3动作迁移-角色一致性图生视频工作流_2087345943531311106.json, 视频生成/文生视频/MinimaxH3开源版参考生视频｜9-3-3高质量生成_2095584855844278273.json, 视频生成/文生视频/全模态多参考视频生成器｜MiniMax H3一键直出_2090902980487892993.json, 视频生成/文生视频/全模态多参考视频生成器｜MiniMax H3文生图生视频_2092019899022528514.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_241

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/H3动作迁移 参考视频动作迁移角色一致性生成_2099923089667747842.json、视频生成/图生视频/MINIMAX-H3动作迁移-角色一致性图生视频工作流_2087345943531311106.json、视频生成/文生视频/MinimaxH3开源版参考生视频｜9-3-3高质量生成_2095584855844278273.json、视频生成/文生视频/全模态多参考视频生成器｜MiniMax H3一键直出_2090902980487892993.json、视频生成/文生视频/全模态多参考视频生成器｜MiniMax H3文生图生视频_2092019899022528514.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetVideoComponents` —— 4/5 个有
- `LoadVideo` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `LoadAudio` —— 3/5 个有
- `AILab_ImageStitch` —— 2/5 个有
- `CM_IntToFloat` —— 2/5 个有
- `CR Prompt Text` —— 2/5 个有
- `JoinStrings` —— 2/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/5 个有
- `RHHiddenNodes` —— 2/5 个有
- `easy int` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `ShellAgentPluginOutputText` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `easy anythingIndexSwitch` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `llama_cpp_instruct_adv` —— 1/5 个有
- `llama_cpp_model_loader` —— 1/5 个有
- `llama_cpp_parameters` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
