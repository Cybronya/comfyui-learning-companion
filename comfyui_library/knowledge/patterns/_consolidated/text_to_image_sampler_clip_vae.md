---
name: text_to_image_sampler_clip_vae
type: Text To Image
frequency: 37
level: strong
coverage: 0.984216
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux-提取图像人物服装_1996180495828467714.json, 图片生成/图生图/FluxKontext2image_双图参考基础版_BORGES_1951577694192480257.json, 图片生成/图生图/KontextNunchakuDevLora-人物手办_1963768517977935874.json, 图片生成/图生图/KontextNunchakuDevLoraBronze风格_1946467003889512449.json, 图片生成/图生图/KontextNunchakuDevLoraCG动漫画风_1948349437268623362.json, 图片生成/图生图/KontextNunchakuDevLoraFelt风格_1946468864593158145.json, 图片生成/图生图/KontextNunchakuDevLoraMakotoShinkai风格_1945744810374471682.json, 图片生成/图生图/KontextNunchakuDevLoraPVC手办_1947979804409757698.json, 图片生成/图生图/KontextNunchakuDevLoraPin Up 1950 style_1949461756606873602.json, 图片生成/图生图/KontextNunchakuDevLoraQ版画风_1945368890681774081.json, 图片生成/图生图/KontextNunchakuDevLoraSketch风格_1946478529522331649.json, 图片生成/图生图/KontextNunchakuDevLora一键转手办_1949798748291555330.json, 图片生成/图生图/KontextNunchakuDevLora低多边形风格_1948343021386510337.json, 图片生成/图生图/KontextNunchakuDevLora儿童手绘具象化_1946884886051610625.json, 图片生成/图生图/KontextNunchakuDevLora光影斑驳_1947620625810677761.json, 图片生成/图生图/KontextNunchakuDevLora刺绣风格_1948369248132431874.json, 图片生成/图生图/KontextNunchakuDevLora变成胖子beta_1944276142456995841.json, 图片生成/图生图/KontextNunchakuDevLora变胖130斤_1944270059869179906.json, 图片生成/图生图/KontextNunchakuDevLora吉卜力风格转绘_1949459998803427329.json, 图片生成/图生图/KontextNunchakuDevLora后视图_1945363825480880129.json, 图片生成/图生图/KontextNunchakuDevLora图案提取_1949463514952937474.json, 图片生成/图生图/KontextNunchakuDevLora多视角_1945744144364949505.json, 图片生成/图生图/KontextNunchakuDevLora女变男_1944276884266029057.json, 图片生成/图生图/KontextNunchakuDevLora小说推文插画_1945743405722849282.json, 图片生成/图生图/KontextNunchakuDevLora换脸_1948371308489912321.json, 图片生成/图生图/KontextNunchakuDevLora漫画风格_1949466495155372034.json, 图片生成/图生图/KontextNunchakuDevLora男变女_1944274798719668226.json, 图片生成/图生图/KontextNunchakuDevLora精修万物_1945012721181188098.json, 图片生成/图生图/KontextNunchakuDevLora线稿上色_1947618380012544002.json, 图片生成/图生图/KontextNunchakuDevLora线稿上色_1949457921794027522.json, 图片生成/图生图/KontextNunchakuDevLora老照片风格_1946476951588757506.json, 图片生成/图生图/KontextNunchakuDevLora金属雕塑工艺品_1947977542977368066.json, 图片生成/图生图/KontextNunchakuDevLora镜头拉远_1947984712961785857.json, 图片生成/图生图/KontextNunchakuDevLora青春变形记风格_1944278493272113153.json, 图片生成/图生图/Kontext双图融合(Nunchaku超级加速)_1938454120015527937.json, 图片生成/图生图/USO平替KontextNunchakuDevLora-人物+物品+换背景和动作_1963042557133565954.json, 平台全量/Kontext换装(虚拟试穿)_1940304113307439106.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae

> 由 `engine/knowledge_consolidation` 从 37 个 workflow 归纳得出（图片生成/图生图/Flux-提取图像人物服装_1996180495828467714.json、图片生成/图生图/FluxKontext2image_双图参考基础版_BORGES_1951577694192480257.json、图片生成/图生图/KontextNunchakuDevLora-人物手办_1963768517977935874.json、图片生成/图生图/KontextNunchakuDevLoraBronze风格_1946467003889512449.json、图片生成/图生图/KontextNunchakuDevLoraCG动漫画风_1948349437268623362.json…）

- **类型**：Text To Image
- **样本数**：37
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 37 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 35/37 个有
- `NunchakuFluxDiTLoader` —— 35/37 个有
- `RH_Translator` —— 35/37 个有
- `LoraLoaderModelOnly` —— 34/37 个有
- `ModelSamplingFlux` —— 33/37 个有
- `ImageStitch` —— 12/37 个有
- `PreviewImage` —— 12/37 个有
- `UNETLoader` —— 3/37 个有
- `Bjornulf_ShowStringText` —— 2/37 个有
- `GetImageSize` —— 2/37 个有
- `UnetLoaderGGUF` —— 2/37 个有
- `CheckpointLoaderSimple` —— 1/37 个有
- `LoraLoader` —— 1/37 个有
- `Note Plus (mtb)` —— 1/37 个有
- `RH_Captioner` —— 1/37 个有
- `RMBG` —— 1/37 个有
- `TTP_text_mix` —— 1/37 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 37 | 100% |
| 高度 | 1536 | 1024 - 1536 | 37 | 89% |
| 采样步数 | 20 | 10 - 20 | 37 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 37 | 100% |
| 采样算法 | euler | - | 37 | 100% |
| 调度器 | simple | - | 37 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 37 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，37 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1024 - 1536，37 个样本，取值集中（一致性 89%）
- 采样步数 中位数 20，观测区间 10 - 20，37 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，37 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，37 个样本，一致性 100%
- 调度器 最常用 simple，37 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，37 个样本，取值集中（一致性 100%）
