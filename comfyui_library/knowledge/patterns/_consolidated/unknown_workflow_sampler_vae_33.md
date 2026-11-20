---
name: unknown_workflow_sampler_vae_33
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.928545
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus_lrzjason, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit人物多角度生成_1987876249525751810.json, 图片生成/图生图/Qwen edit-图像编辑加强版_1991875959590809602.json, 图片生成/图生图/Qwen-Edit-2511人像一致性写真_2004346764650053633.json, 图片生成/图生图/Qwen-Edit-Nunchaku加速版人物一致性写真图生成_1991879930273222658.json, 图片生成/图生图/Qwen-Edit-人像一致性写真图升级版_1990409634555072513.json, 图片生成/图生图/Qwen-edit-2511 IP形象三视图_2005165387983585282.json, 图片生成/图生图/Qwen-edit-2511 参考角色一致性 最强好用版_2005163754126016513.json, 图片生成/文生图/Qwen-Edit-电影分镜一致性图像生成_1990781739645743105.json, 图片生成/文生图/Qwen-edit-测试用工作流_2007743754337259522.json, 平台全量/Qwen edit plus-nunchaku4步出图_1973011148134027265.json, 平台全量/Qwen edit plus-nunchaku8步出图_1973017136211865601.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_33

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen Edit人物多角度生成_1987876249525751810.json、图片生成/图生图/Qwen edit-图像编辑加强版_1991875959590809602.json、图片生成/图生图/Qwen-Edit-2511人像一致性写真_2004346764650053633.json、图片生成/图生图/Qwen-Edit-Nunchaku加速版人物一致性写真图生成_1991879930273222658.json、图片生成/图生图/Qwen-Edit-人像一致性写真图升级版_1990409634555072513.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/11 个有
- `LoraLoaderModelOnly` —— 10/11 个有
- `JDCN_StringToList` —— 7/11 个有
- `AILab_QwenVL` —— 6/11 个有
- `UNETLoader` —— 6/11 个有
- `easy showAnything` —— 6/11 个有
- `NunchakuQwenImageDiTLoader` —— 5/11 个有
- `MuyeTextEditOutput` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `PrimitiveStringMultiline` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 11 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 64% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
