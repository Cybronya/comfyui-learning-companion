---
name: unknown_workflow_sampler_checkpoint_vae_2
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.941316
common_nodes: [CLIPVisionEncode, EmptyLatentHunyuan3Dv2, ImageOnlyCheckpointLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveGLB, SaveImage, VAEDecodeHunyuan3D]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/006.Hunyuan模型创建002.多视图生成3D模型_2035389695059824642.json, 图片生成/图生图/Hunyuan3D-多视图生成glb模型_2074612521968955394.json, 图片生成/图生图/一键3D模型，图转3D，手办玩具设计，3D打印_2032143682186514433.json, 图片生成/图生图/上传一张图片即可得到它的3D模型，王炸混元3D+2.1_2016310657410408450.json, 图片生成/图生图/官方混元3D-v2.1 工作流 V1.0_1988070322928857090.json, 图片生成/图生图/混元3D-v2.1_1970105286205841410.json, 图片生成/图生图/混元3D-v2.1_2013566476392861698.json, 图片生成/图生图/自己用：建模_1966308326344658945.json, 图片生成/文生图/混元3D 2.1(Comfy官方版)V1_1966105526599847937.json, 平台全量/3d_hunyuan3d-v2.1_2014495028529336321.json, 平台全量/Hunyuan3D 2.1单视图模型生成标准版_2069034130460987394.json, 平台全量/hunyuan-3d建模_1962040045551206401.json, 平台全量/hunyuan3D开源-图像图片转3D建模模型_2091182231606874114.json, 平台全量/上传一张图片即可得到它的3D模型，王炸混元3D 2.1(Comfy官方版)建模师要下岗了？_1966419721505681410.json, 平台全量/图转3D混元Hunyuan3D-2（输入图片生成3D模型）_2015259765357682690.json, 平台全量/多视图图像转 3D 模型（Hunyuan3D-2mv）_1904419126130155522.json, 平台全量/混元3D 2.1(Comfy官方版)V1_1966133340032110593.json, 平台全量/混元3D-v2.1_1993200406207594498.json, 平台全量/混元3D-三视图转3D comfy官网版_1906756215303720962.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_2

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/006.Hunyuan模型创建002.多视图生成3D模型_2035389695059824642.json、图片生成/图生图/Hunyuan3D-多视图生成glb模型_2074612521968955394.json、图片生成/图生图/一键3D模型，图转3D，手办玩具设计，3D打印_2032143682186514433.json、图片生成/图生图/上传一张图片即可得到它的3D模型，王炸混元3D+2.1_2016310657410408450.json、图片生成/图生图/官方混元3D-v2.1 工作流 V1.0_1988070322928857090.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPVisionEncode`
- `EmptyLatentHunyuan3Dv2`
- `ImageOnlyCheckpointLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveGLB`
- `SaveImage`
- `VAEDecodeHunyuan3D`

**可变部分**（部分 workflow 才有）：
- `Hunyuan3Dv2Conditioning` —— 14/19 个有
- `VoxelToMesh` —— 14/19 个有
- `VoxelToMeshBasic` —— 11/19 个有
- `Hunyuan3Dv2ConditioningMultiView` —— 6/19 个有
- `easy imageRemBg` —— 6/19 个有
- `EmptyImage` —— 1/19 个有
- `Fast Bypasser (rgthree)` —— 1/19 个有
- `ImageCrop` —— 1/19 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 4096 | 3072 - 8192 | 19 | 57% |
| 高度 | 1 | 1 - 1 | 19 | 100% |
| 采样步数 | 20 | 20 - 50 | 19 | 70% |
| Prompt 约束强度(CFG) | 7.5 | 5 - 8 | 19 | 79% |
| 采样算法 | euler | - | 19 | 100% |
| 调度器 | normal | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 19/19 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 4096，观测区间 3072 - 8192，19 个样本
- 高度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 50，19 个样本
- Prompt 约束强度(CFG) 中位数 7.5，观测区间 5 - 8，19 个样本
- 采样算法 最常用 euler，19 个样本，一致性 100%
- 调度器 最常用 normal，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（19/19 个样本）：发现KSampler但没有VAEDecode
