---
name: image_to_image_sampler_vae_9
type: Image To Image
frequency: 11
level: strong
coverage: 0.917818
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, ModelSamplingAuraFlow, QwenMultiangleCameraNode, SaveImage, TextEncodeQwenImageEditPlus, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/Qwen2511-控制角度工作流_2077302736273629186.json, 图片生成/图生图/Qwen2511控制照片角度工作流_2016442774928756738.json, 图片生成/图生图/Qwen_Multiangle_2511自由控制图片角度_2038555716276981761.json, 图片生成/图生图/edit_2511图像多角度编辑_2009951290171854849.json, 图片生成/图生图/image_qwen_image_edit_2511-单图参考+运镜_2010906708750639106.json, 图片生成/图生图/image_qwen_image_edit_2511_multiangle_camera 尺寸2K限_2019265588102701057.json, 图片生成/图生图/image_qwen_image_edit_2511_multiangle_camera_2010682508362391554.json, 图片生成/图生图/image_qwen_image_edit_2511_multiangle_camera转角度_2018618986367291394.json, 图片生成/图生图/qwen 多视图 三视图 图生图  相机镜头控制器_2039644703557165058.json, 图片生成/图生图/qwen 精准镜头控制器 多视图 三视图 图生图_2039526686571634689.json, 图片生成/文生图/图片多角度工作流_2009868602559696897.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_9

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen2511-控制角度工作流_2077302736273629186.json、图片生成/图生图/Qwen2511控制照片角度工作流_2016442774928756738.json、图片生成/图生图/Qwen_Multiangle_2511自由控制图片角度_2038555716276981761.json、图片生成/图生图/edit_2511图像多角度编辑_2009951290171854849.json、图片生成/图生图/image_qwen_image_edit_2511-单图参考+运镜_2010906708750639106.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 9/11 个有
- `LoraLoaderModelOnly` —— 9/11 个有
- `UNETLoader` —— 9/11 个有
- `VAEDecode` —— 8/11 个有
- `ShowText|pysssss` —— 5/11 个有
- `PreviewImage` —— 3/11 个有
- `VAEDecodeTiled` —— 3/11 个有
- `CheckpointLoaderSimple` —— 2/11 个有
- `ImpactMakeAnyList` —— 2/11 个有
- `StringConcatenate` —— 2/11 个有
- `图像缩放范围孤海` —— 2/11 个有
- `String` —— 1/11 个有
- `easy promptList` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 11 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 3/11 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
