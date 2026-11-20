---
name: unknown_workflow_lora_sampler_checkpoint
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.777778
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 人物证件照无水印版_2019647692418322433.json, 图片生成/图生图/Qwen-Rapid-AIO电商产品溶图矫正角度，重新纠正光源_2054467334085062657.json, 图片生成/图生图/Qwen-Rapid-AIO电商产品溶图矫正角度，重新纠正光源_2057720344152207361.json, 图片生成/图生图/一键证件照自动美颜+换发型_服装万能证件照_2079884897178705922.json, 图片生成/图生图/一键证件照自动美颜+换发型_服装万能证件照_2080470101836517377.json, 图片生成/图生图/全能电商产品溶图自动矫正角度，重新纠正光源_2041830014605336577.json, 图片生成/图生图/电商产品溶图 图生图_2034458183934152705.json, 图片生成/图生图/电商产品溶图，自动矫正角度，重新纠正光源_2101208468156936194.json, 图片生成/图生图/电商产品溶图，自动矫正角度，重新纠正光源_2102202784425799681.json, 平台全量/Qwen AIO 2511万能证件照_1997192304547020801.json, 平台全量/Qwen+AIO+2511万能证件照_2019212583181488129.json, 平台全量/一键证件照（自动美颜+换发型_服装）万能证件照_2078765698955964418.json, 平台全量/一键转红蓝底证件照 （带美颜+换装）可手机上传照片_2063791301962854401.json, 平台全量/万能证件照 一键证件照（自动美颜+换发型_服装）证件照 Qwen AIO 2511_2019952072686309377.json, 平台全量/万能证件照 一键运行（带美颜+换装）_2045763299463139329.json, 平台全量/电商产品溶图，自动矫正角度，重新纠正光源_1997283440359849986.json, 平台全量/电商产品溶图，自动矫正角度，重新纠正光源_2020380768333209601.json, 平台全量/电商产品溶图，自动矫正角度，重新纠正光源_2046140755231641602.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/Qwen 人物证件照无水印版_2019647692418322433.json、图片生成/图生图/Qwen-Rapid-AIO电商产品溶图矫正角度，重新纠正光源_2054467334085062657.json、图片生成/图生图/Qwen-Rapid-AIO电商产品溶图矫正角度，重新纠正光源_2057720344152207361.json、图片生成/图生图/一键证件照自动美颜+换发型_服装万能证件照_2079884897178705922.json、图片生成/图生图/一键证件照自动美颜+换发型_服装万能证件照_2080470101836517377.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 18 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 10/18 个有
- `CR Prompt Text` —— 9/18 个有
- `Int` —— 9/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/18 个有
- `easy cleanGpuUsed` —— 9/18 个有
- `Image Crop Face` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4.5 | 4 - 5 | 18 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | lcm | - | 18 | 50% |
| 调度器 | normal | - | 18 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 1020 | 1016 - 1024 | 18 | 100% |
| 高度 | 1488 | 1440 - 1536 | 18 | 97% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4.5，观测区间 4 - 5，18 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，18 个样本，一致性 50%
- 调度器 最常用 normal，18 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 1020，观测区间 1016 - 1024，18 个样本，取值集中（一致性 100%）
- 高度 中位数 1488，观测区间 1440 - 1536，18 个样本，取值集中（一致性 97%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
