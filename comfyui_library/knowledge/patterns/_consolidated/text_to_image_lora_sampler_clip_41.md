---
name: text_to_image_lora_sampler_clip_41
type: Text To Image
frequency: 17
level: strong
coverage: 0.925647
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, MiniMaxH3TurboLoRA, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/带放大功能｜Minimax H3文生图榨干功能性_2091175836807421954.json, 视频生成/图生视频/AI萌宠视频工作流｜宠物带货15秒1080P图生视频生成_2096730470561181698.json, 视频生成/图生视频/MiniMax H3单图参考AI图生视频极速10秒1080P处理工具_2101775568348995586.json, 视频生成/图生视频/MiniMax H3模仿跳舞工作流，动作迁移舞蹈模仿自动生成提示词图生视频_2103629203055931394.json, 视频生成/图生视频/Minima H3多图参考生视频工作流 极速15秒1080P_2108994634998435842.json, 视频生成/图生视频/Minimax H3单图生视频工作流极速15秒1080P 高质量动态生成_2108624319713734657.json, 视频生成/图生视频/Minimax H3单图生视频｜极速15秒直出1080P高清成片_2108394651400105985.json, 视频生成/图生视频/Minimax H3模仿跳舞工作流动作迁移舞蹈模仿自动生成提示词_2108649647211372545.json, 视频生成/图生视频/唱歌对口型数字人｜Minimax H3含提示词模版视频_2092744057880666114.json, 视频生成/图生视频/超强宠物带货15秒萌宠视频生成_2102974255624450049.json, 视频生成/文生视频/Minimax H3文生视频4步加速｜支持15秒1080P高清_2108415635075190785.json, 视频生成/文生视频/Minimax H3文生视频工作流4步加速支持15秒1080P 快速出片_2108632313293795329.json, 视频生成/文生视频/写实加速工作流｜Minimax H3多参考10秒1080P_2090923852997156866.json, 视频生成/文生视频/多图参考生视频｜Minimax超级好用一键生成_2094755410006855681.json, 视频生成/文生视频/宠物带货15秒1080P｜Minimax H3萌宠视频图生视频_2092889992501747713.json, 视频生成/文生视频/宠物带货15秒1080P｜Minimax H3萌宠视频生成_2092701213329547265.json, 音频生成/音频生成/AI音乐声音克隆｜Minimax H3超长生成多音频参考_2091182922152890370.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/带放大功能｜Minimax H3文生图榨干功能性_2091175836807421954.json、视频生成/图生视频/AI萌宠视频工作流｜宠物带货15秒1080P图生视频生成_2096730470561181698.json、视频生成/图生视频/MiniMax H3单图参考AI图生视频极速10秒1080P处理工具_2101775568348995586.json、视频生成/图生视频/MiniMax H3模仿跳舞工作流，动作迁移舞蹈模仿自动生成提示词图生视频_2103629203055931394.json、视频生成/图生视频/Minima H3多图参考生视频工作流 极速15秒1080P_2108994634998435842.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyModelAdapter`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3TurboLoRA`
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 16/17 个有
- `SaveVideo` —— 16/17 个有
- `SpectrumApplyMiniMaxH3` —— 16/17 个有
- `LoadImage` —— 11/17 个有
- `ExtendIntermediateSigmas` —— 8/17 个有
- `SaveImage` —— 7/17 个有
- `LoadVideo` —— 5/17 个有
- `LoadAudio` —— 4/17 个有
- `PDGeminiAPIKey` —— 2/17 个有
- `PreviewAudio` —— 2/17 个有
- `PreviewTextNode` —— 2/17 个有
- `GetImagesFromBatchIndexed` —— 1/17 个有
- `ImageUpscaleWithModel` —— 1/17 个有
- `PreviewImage` —— 1/17 个有
- `UpscaleModelLoader` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
