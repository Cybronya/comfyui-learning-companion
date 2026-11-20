---
name: unknown_workflow_lora_sampler_clip_12
type: Unknown Workflow
frequency: 21
level: strong
coverage: 0.99719
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/80年底复古漫画_1966400010009128961.json, 图片生成/图生图/Kontext_超级屏幕联动（快速读取软件窗口图像）_1949855964494217217.json, 图片生成/图生图/一键手绘插画风格_1964963061075464194.json, 图片生成/图生图/厚涂漫画风格_1966390699019153410.json, 图片生成/图生图/变淡水彩_1964545521945858050.json, 图片生成/图生图/图片风格插画化_1966399479161270273.json, 图片生成/图生图/手绘美漫风格转绘_1964908268000788481.json, 图片生成/图生图/日常照片写真转绘卡通动画_1964909780139692034.json, 图片生成/图生图/昭和复古动漫风格_1964965180033650690.json, 图片生成/图生图/水下摄影_1964584753322147841.json, 图片生成/图生图/水彩风宠物转绘_1964900906997305346.json, 图片生成/图生图/治愈风漫画_1966401018340782082.json, 图片生成/图生图/瑞克·摩特里美式漫画_1964969597982134274.json, 图片生成/图生图/真人转蜡笔画风格_1964972661124288514.json, 图片生成/图生图/精美二次元风格_1964971064684068866.json, 图片生成/图生图/转创意油画_1964590628837408770.json, 图片生成/图生图/转吉卜力风格_1964556154326106113.json, 图片生成/图生图/转国风_1964588333903040514.json, 图片生成/图生图/转手绘卡通_1964580745543077890.json, 图片生成/图生图/转手绘时尚插画_1964587060856242177.json, 图片生成/图生图/转黑白手绘插画_1964904635557363714.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/80年底复古漫画_1966400010009128961.json、图片生成/图生图/Kontext_超级屏幕联动（快速读取软件窗口图像）_1949855964494217217.json、图片生成/图生图/一键手绘插画风格_1964963061075464194.json、图片生成/图生图/厚涂漫画风格_1966390699019153410.json、图片生成/图生图/变淡水彩_1964545521945858050.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: FluxKontextImageScale` —— 20/21 个有
- `LoadImageFromURL` —— 20/21 个有
- `DeepTranslatorTextNode` —— 1/21 个有
- `FloatingVideo` —— 1/21 个有
- `FluxKontextImageScale` —— 1/21 个有
- `PreviewImage` —— 1/21 个有
- `ScreenShare` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 21 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 21 | 100% |
| 采样算法 | euler | - | 21 | 100% |
| 调度器 | simple | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，21 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，21 个样本，一致性 100%
- 调度器 最常用 simple，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
