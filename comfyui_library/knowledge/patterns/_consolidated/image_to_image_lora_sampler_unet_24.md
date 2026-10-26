---
name: image_to_image_lora_sampler_unet_24
type: Image To Image
frequency: 17
level: strong
coverage: 0.903059
common_nodes: [CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen2511分镜头制作_2013613666763022338.json, 图片生成/图生图/qwen_edit_2511镜头视角控制_2010636578489634817.json, 图片生成/图生图/三图编辑_2067961763567591425.json, 图片生成/图生图/人物视角转换_2009456601119334402.json, 图片生成/图生图/人物视角转换_2065426763504775169.json, 图片生成/图生图/全量qwen edit 2512单图多角度编辑工作流_2068339692986265601.json, 图片生成/图生图/分镜一键九视图短剧分镜一键版人物一致性（2分钟版）qwen2511_2010271091205349378.json, 图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2009533490206871553.json, 图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2083366341913960449.json, 图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2083375355112550402.json, 图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2091742231643381762.json, 图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2101961996269871105.json, 图片生成/图生图/场景多角度分镜4.0((九视角）制作镜头qwen2511风格一致性分镜加速版4.0_2018924258122010625.json, 图片生成/图生图/多场景 多角度 分镜制作 qwen2511 风格一致性 分镜加速版3.0_2046210559363780610.json, 图片生成/图生图/多视角影视人物多视角加速版（常用视角）_2009573649203863554.json, 图片生成/图生图/小说分镜漫剧短剧剧本（大师级分镜可控）一键九视图短剧分镜一键版人物一致性（2分钟版）qwen2511_2021774358364033025.json, 图片生成/图生图/漫剧短剧分镜剧本（大师级分镜可控）一键九视图短剧分镜一键版人物一致性（2分钟版）qwen2511_2019360805640212482.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_24

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/qwen2511分镜头制作_2013613666763022338.json、图片生成/图生图/qwen_edit_2511镜头视角控制_2010636578489634817.json、图片生成/图生图/三图编辑_2067961763567591425.json、图片生成/图生图/人物视角转换_2009456601119334402.json、图片生成/图生图/人物视角转换_2065426763504775169.json…）

- **类型**：Image To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 16/17 个有
- `FluxKontextImageScale` —— 15/17 个有
- `CR Prompt List` —— 11/17 个有
- `PreviewAny` —— 11/17 个有
- `Text Multiline` —— 11/17 个有
- `AILab_QwenVL` —— 4/17 个有
- `CR Prompt Text` —— 4/17 个有
- `JDCN_StringToList` —— 4/17 个有
- `QwenMultiangleCameraNode` —— 4/17 个有
- `ShowText|pysssss` —— 4/17 个有
- `ProcessString` —— 2/17 个有
- `YC_textReplaceNode` —— 2/17 个有
- `easy promptLine` —— 2/17 个有
- `CR Text` —— 1/17 个有
- `easy promptConcat` —— 1/17 个有
- `easy promptList` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 17 | 100% |
| 采样算法 | euler | - | 17 | 100% |
| 调度器 | simple | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，17 个样本，一致性 100%
- 调度器 最常用 simple，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
