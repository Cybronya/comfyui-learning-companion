---
name: image_to_image_sampler_unet_vae_14
type: Image To Image
frequency: 9
level: moderate
coverage: 0.869556
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/8步加速-QwenEdit位置偏移解决方案_1968478135140397058.json, 图片生成/图生图/FireRed_图生图_2029829360181583873.json, 图片生成/图生图/QWEN-Edit-2509 单图 + 多图编辑_1971122834372206593.json, 图片生成/图生图/QWEN-Edit-2509 单图 + 多图编辑_1984428089918832641.json, 图片生成/图生图/Qwen-Edit-2509 CN 控制参考，图像编辑_1971156046700023809.json, 图片生成/图生图/QwenEdit-Instyle图像编辑V0.5_1968547479576825858.json, 图片生成/图生图/QwenEdit-万物竖中指一致性图像编辑V1_1968543069031288833.json, 图片生成/图生图/QwenEdit-电商服装人台V1（不支持真人）_1968545752215629825.json, 图片生成/图生图/（志佬开源）QwenEdit一致性图像编辑V2_1968246710134812674.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_14

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/8步加速-QwenEdit位置偏移解决方案_1968478135140397058.json、图片生成/图生图/FireRed_图生图_2029829360181583873.json、图片生成/图生图/QWEN-Edit-2509 单图 + 多图编辑_1971122834372206593.json、图片生成/图生图/QWEN-Edit-2509 单图 + 多图编辑_1984428089918832641.json、图片生成/图生图/Qwen-Edit-2509 CN 控制参考，图像编辑_1971156046700023809.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 8/9 个有
- `Image Comparer (rgthree)` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `ImageConcanate` —— 7/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 5/9 个有
- `CR Prompt Text` —— 4/9 个有
- `Text Multiline` —— 4/9 个有
- `TextEncodeQwenImageEditPlus` —— 4/9 个有
- `RH_LLMAPI_NODE` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `CR Simple Image Compare` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `TextEncodeQwenImageEdit` —— 2/9 个有
- `AIO_Preprocessor` —— 1/9 个有
- `NunchakuQwenImageDiTLoader` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 9 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 9 | 53% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | beta57 | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，9 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 beta57，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
