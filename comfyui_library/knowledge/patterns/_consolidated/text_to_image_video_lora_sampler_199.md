---
name: text_to_image_video_lora_sampler_199
type: Text To Image
frequency: 3
level: strong
coverage: 0.780333
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, JjkText, KSampler, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8GH, MiniMaxH3DualClockT8GH, MiniMaxH3IntegrationAdapterGH, MiniMaxH3IntegrationGH, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy anythingIndexSwitch, easy ifElse, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/ComfyUI多轮对话Skill加载｜配合MiniMax-H3智能工作台_2092077272688844801.json, 视频生成/文生视频/H3极简视频工作台｜文生音频图生视频三合一_2091666153218334722.json, 视频生成/文生视频/智能一体化视频创作｜MiniMax H3优化版文生图生视频_2090533006632116225.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_199

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/ComfyUI多轮对话Skill加载｜配合MiniMax-H3智能工作台_2092077272688844801.json、视频生成/文生视频/H3极简视频工作台｜文生音频图生视频三合一_2091666153218334722.json、视频生成/文生视频/智能一体化视频创作｜MiniMax H3优化版文生图生视频_2090533006632116225.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8GH`
- `MiniMaxH3DualClockT8GH`
- `MiniMaxH3IntegrationAdapterGH`
- `MiniMaxH3IntegrationGH`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `easy ifElse`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `DapaoAPIChatMaterialLibraryNode` —— 1/3 个有
- `DapaoAPIChatSettingsNode` —— 1/3 个有
- `DapaoAPILLMConfigNode` —— 1/3 个有
- `DapaoAPIMultiTurnChatNode` —— 1/3 个有
- `DapaoAPISkillLoaderNode` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `LoadVideo` —— 1/3 个有
- `LoadVideoNode` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
