---
name: unknown_workflow_sampler_clip_vae_2
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.992778
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/JOJO 动漫风格生成海报_1942397491436523522.json, 图片生成/图生图/Kontext GGUF轻量级模型工作流_1940778080027963393.json, 图片生成/图生图/Kontext [dev] + LoRA + 图像编辑_1938517065856647169.json, 图片生成/图生图/Kontext [dev] + LoRA 模型｜吉卜力风格_1938993796610711554.json, 图片生成/图生图/Kontext [dev] + LoRA 模型｜风格控制_1938878555705298945.json, 图片生成/图生图/Kontext dev 8bit 像素艺术风格_1945444470357938178.json, 图片生成/图生图/Kontext dev 毛玻璃棱镜风格_1941720796366848001.json, 图片生成/图生图/Kontext dev 蓬松毛毡风格_1941688670523125762.json, 图片生成/图生图/Kontext dev｜JOJO 日系动漫风格_1942035838689820673.json, 图片生成/图生图/KontextNunchakuDev动漫风尺寸可调节_1943514272796188673.json, 图片生成/图生图/KontextNunchakuDev风格尺寸可调节_1943517928019161090.json, 图片生成/图生图/Kontext｜乐高积木风格_1942893098185662466.json, 图片生成/图生图/Kontext｜扁平邮票插画风格_1946923634122481665.json, 图片生成/图生图/Kontext｜美式漫画风格_1942237284731138049.json, 图片生成/图生图/动漫人物 cosplay｜Kontext_1962014034272915458.json, 图片生成/图生图/模特项链试戴展示 单图生成_1947197718127136769.json, 图片生成/图生图/泡泡玛特 molly 风格人物｜Kontext_1951568255880253442.json, 图片生成/图生图/苹果 Emoji 风格人物｜Kontext_1948330346327736321.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_2

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/JOJO 动漫风格生成海报_1942397491436523522.json、图片生成/图生图/Kontext GGUF轻量级模型工作流_1940778080027963393.json、图片生成/图生图/Kontext [dev] + LoRA + 图像编辑_1938517065856647169.json、图片生成/图生图/Kontext [dev] + LoRA 模型｜吉卜力风格_1938993796610711554.json、图片生成/图生图/Kontext [dev] + LoRA 模型｜风格控制_1938878555705298945.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 15/18 个有
- `LoraLoaderModelOnly` —— 14/18 个有
- `ImageSizeInfo` —— 10/18 个有
- `ModelSamplingFlux` —— 7/18 个有
- `easy imageConcat` —— 6/18 个有
- `NunchakuFluxDiTLoader` —— 2/18 个有
- `RH_Translator` —— 2/18 个有
- `DeepTranslatorCLIPTextEncodeNode` —— 1/18 个有
- `GetImageSize` —— 1/18 个有
- `ImageScaleBy` —— 1/18 个有
- `SDXLPromptStyler` —— 1/18 个有
- `UnetLoaderGGUF` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
