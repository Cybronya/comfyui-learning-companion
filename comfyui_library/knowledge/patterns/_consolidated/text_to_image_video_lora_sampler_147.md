---
name: text_to_image_video_lora_sampler_147
type: Text To Image
frequency: 4
level: strong
coverage: 0.8345
common_nodes: [BasicScheduler, BerniniConditioning, BerniniPromptEnhancer, CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageConcanate, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewAny, PrimitiveInt, SamplerCustom, SplitSigmas, TextConcatenate, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/BERNINI动作迁移视频换脸｜WAN2.2图生视频工作流_2088358664938807297.json, 视频生成/图生视频/BERNINI视频换脸动作迁移｜WAN2.2图生视频角色驱动_2090546400839946242.json, 视频生成/图生视频/WAN2.2 BERNINI视频换脸动作迁移 图生视频角色精准驱动_2092549781938851841.json, 视频生成/图生视频/动作迁移视频WAN2.2 BERNINI图生视频视频换脸工作流_2088388446917324801.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_147

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/BERNINI动作迁移视频换脸｜WAN2.2图生视频工作流_2088358664938807297.json、视频生成/图生视频/BERNINI视频换脸动作迁移｜WAN2.2图生视频角色驱动_2090546400839946242.json、视频生成/图生视频/WAN2.2 BERNINI视频换脸动作迁移 图生视频角色精准驱动_2092549781938851841.json、视频生成/图生视频/动作迁移视频WAN2.2 BERNINI图生视频视频换脸工作流_2088388446917324801.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `BerniniConditioning`
- `BerniniPromptEnhancer`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageConcanate`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveInt`
- `SamplerCustom`
- `SplitSigmas`
- `TextConcatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
