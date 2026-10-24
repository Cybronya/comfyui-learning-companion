---
name: text_to_image_video_lora_sampler_126
type: Text To Image
frequency: 6
level: strong
coverage: 0.842
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMaxH3图生视频场景特效直出_2093415902871121922.json, 视频生成/文生视频/MiniMaxH3多图数字人生成｜文生视频多图驱动_2094504932195000321.json, 视频生成/文生视频/minimax阿里8步加速三合一｜文生视频图生视频全能参考_2095568310212587522.json, 视频生成/文生视频/像素幻想Lab出品｜MiniMaxH3图生视频场景特效_2093741804817567745.json, 视频生成/文生视频/多图数字人生成｜MiniMaxH3文生图生视频工作流_2094729429032464385.json, 视频生成/文生视频/文生图生视频全能参考三合一｜minimax阿里8步加速_2095811801366745089.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_126

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/MiniMaxH3图生视频场景特效直出_2093415902871121922.json、视频生成/文生视频/MiniMaxH3多图数字人生成｜文生视频多图驱动_2094504932195000321.json、视频生成/文生视频/minimax阿里8步加速三合一｜文生视频图生视频全能参考_2095568310212587522.json、视频生成/文生视频/像素幻想Lab出品｜MiniMaxH3图生视频场景特效_2093741804817567745.json、视频生成/文生视频/多图数字人生成｜MiniMaxH3文生图生视频工作流_2094729429032464385.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `MiniMaxH3ImageToVideo` —— 4/6 个有
- `MiniMaxH3ReferenceToVideo` —— 4/6 个有
- `PrimitiveFloat` —— 4/6 个有
- `ShowText|pysssss` —— 4/6 个有
- `VAEDecodeAudio` —— 4/6 个有
- `llama_cpp_instruct_adv` —— 4/6 个有
- `llama_cpp_model_loader` —— 4/6 个有
- `llama_cpp_parameters` —— 4/6 个有
- `Audio Duration (mtb)` —— 2/6 个有
- `AudioCrop` —— 2/6 个有
- `AudioSeparation` —— 2/6 个有
- `LoadAudio` —— 2/6 个有
- `MathExpression|pysssss` —— 2/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/6 个有
- `ModelAttentionBackend` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/6 个有
- `easy float` —— 2/6 个有

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
