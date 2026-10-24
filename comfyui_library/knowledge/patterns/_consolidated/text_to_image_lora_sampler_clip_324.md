---
name: text_to_image_lora_sampler_clip_324
type: Text To Image
frequency: 6
level: strong
coverage: 0.872167
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3动作迁移 参考视频动作迁移角色一致性生成_2099923089667747842.json, 视频生成/图生视频/MINIMAX-H3动作迁移-角色一致性图生视频工作流_2087345943531311106.json, 视频生成/图生视频/多图生视频+音频+视频接入｜MiniMax H3场景特效_2092205364438720514.json, 视频生成/图生视频/多图生视频音频视频接入｜MiniMax H3场景特效生成_2092018470065106945.json, 视频生成/图生视频/海螺MiniMax-H3开源版图片开口说话数字人-图像音频参考图生视频_2087385959053742082.json, 视频生成/文生视频/MinimaxH3开源版参考生视频｜9-3-3高质量生成_2095584855844278273.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_324

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/H3动作迁移 参考视频动作迁移角色一致性生成_2099923089667747842.json、视频生成/图生视频/MINIMAX-H3动作迁移-角色一致性图生视频工作流_2087345943531311106.json、视频生成/图生视频/多图生视频+音频+视频接入｜MiniMax H3场景特效_2092205364438720514.json、视频生成/图生视频/多图生视频音频视频接入｜MiniMax H3场景特效生成_2092018470065106945.json、视频生成/图生视频/海螺MiniMax-H3开源版图片开口说话数字人-图像音频参考图生视频_2087385959053742082.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
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
- `PrimitiveStringMultiline` —— 5/6 个有
- `GetVideoComponents` —— 4/6 个有
- `LoadAudio` —— 4/6 个有
- `LoadVideo` —— 4/6 个有
- `JoinStrings` —— 3/6 个有
- `AILab_ImageStitch` —— 2/6 个有
- `CM_IntToFloat` —— 2/6 个有
- `CR Prompt Text` —— 2/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/6 个有
- `RHHiddenNodes` —— 2/6 个有
- `easy int` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `AILab_QwenVL` —— 1/6 个有
- `AudioCrop` —— 1/6 个有
- `ShellAgentPluginOutputText` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `easy anythingIndexSwitch` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `llama_cpp_instruct_adv` —— 1/6 个有
- `llama_cpp_model_loader` —— 1/6 个有
- `llama_cpp_parameters` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
