---
name: unknown_workflow_sampler_unet_vae_102
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.994636
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/👾怪獸-多角度分镜批量制作👾_1992884884838608897.json, 平台全量/九视图 多视角人物 _ 场景生成 _ 三视图 _ 广角全身图一键出图_2046570448430829569.json, 平台全量/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2069577487381786625.json, 平台全量/分镜多视图 人物一致 角色模特多角度 多视角 Qwen_Edit_2511_2082653063617269761.json, 平台全量/同一人物不同姿势 一键批量出图多角度 短剧网红 批量调整拍照姿势 拍照姿势多样化_2030124037057286145.json, 平台全量/多视角+角色多视图+多角度++Qwen_Edit_2511_2048931093604212737.json, 平台全量/姿势 动作 角色多视图_多角度_多视角_Qwen_Edit_2511_2048325000750436353.json, 平台全量/角色多视图_多角度_多视角_Qwen_Edit_2511_2021791925199704066.json, 数字人/数字人/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2058378667482509314.json, 数字人/数字人/多角度  多视图  分镜   多视角_2056927991325880322.json, 视频生成/图生视频/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2079109724708102146.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_102

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/👾怪獸-多角度分镜批量制作👾_1992884884838608897.json、平台全量/九视图 多视角人物 _ 场景生成 _ 三视图 _ 广角全身图一键出图_2046570448430829569.json、平台全量/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2069577487381786625.json、平台全量/分镜多视图 人物一致 角色模特多角度 多视角 Qwen_Edit_2511_2082653063617269761.json、平台全量/同一人物不同姿势 一键批量出图多角度 短剧网红 批量调整拍照姿势 拍照姿势多样化_2030124037057286145.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/11 个有
- `easy promptLine` —— 10/11 个有
- `Text Multiline` —— 9/11 个有
- `RHHiddenNodes` —— 1/11 个有
- `easy batchAnything` —— 1/11 个有
- `easy forLoopEnd` —— 1/11 个有
- `easy forLoopStart` —— 1/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
