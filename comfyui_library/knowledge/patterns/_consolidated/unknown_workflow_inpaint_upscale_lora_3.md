---
name: unknown_workflow_inpaint_upscale_lora_3
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.5945
common_nodes: [Any Switch (rgthree), AnySwitch, CFGGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, EmptyFlux2LatentImage, GetImageSize+, InpaintCropImproved, InpaintStitchImproved, JsonExtractString, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ManualSigmas, PreviewImage, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SkipLayerGuidanceDiTSimple, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, easy isNone, 孤海注释]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1古风换脸保五官，SeedVR2超分保住皮肤质感_2116762560254005250.json, 图片生成/图生图/Qwen Image 2.1精准换脸编辑，SeedVR2超分保住皮肤质感_2116395227744395266.json, 图片生成/图生图/Qwen Image 2.1职业照换脸保五官，SeedVR2超分保住皮肤质感_2117120288856039425.json, 平台全量/上传人物图加Cos服参考图一键换装，SeedVR2超分直出写真大图_2117873339233554434.json, 平台全量/上传人物图加旗袍参考图一键换装，SeedVR2超分直出写真大图_2117981312148660225.json, 平台全量/上传人物图加汉服参考图一键换装，SeedVR2超分直出写真大图_2117495832709779458.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_lora_3

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1古风换脸保五官，SeedVR2超分保住皮肤质感_2116762560254005250.json、图片生成/图生图/Qwen Image 2.1精准换脸编辑，SeedVR2超分保住皮肤质感_2116395227744395266.json、图片生成/图生图/Qwen Image 2.1职业照换脸保五官，SeedVR2超分保住皮肤质感_2117120288856039425.json、平台全量/上传人物图加Cos服参考图一键换装，SeedVR2超分直出写真大图_2117873339233554434.json、平台全量/上传人物图加旗袍参考图一键换装，SeedVR2超分直出写真大图_2117981312148660225.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 6 个 workflow 都包含：
- `Any Switch (rgthree)`
- `AnySwitch`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `EmptyFlux2LatentImage`
- `GetImageSize+`
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `JsonExtractString`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SkipLayerGuidanceDiTSimple`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy isNone`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `ImageColorMatch+` —— 2/6 个有
- `ImageRemoveAlpha+` —— 2/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
