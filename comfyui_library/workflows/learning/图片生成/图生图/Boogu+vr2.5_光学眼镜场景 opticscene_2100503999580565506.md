---
key: 图片生成/图生图/Boogu+vr2.5_光学眼镜场景 opticscene_2100503999580565506.json
name: Boogu+vr2.5_光学眼镜场景 opticscene_2100503999580565506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Boogu+vr2.5_光学眼镜场景 opticscene_2100503999580565506.json
hash: 2c2473b8006ee695
coverage: 0.904762
learned_at: 2026-10-10 20:48:02
nodes: [VAELoader, SamplerCustom, DF_Get_image_size, ImageScaleToTotalPixels, KSamplerSelect, ModelSamplingAuraFlow, BasicScheduler, SeedVR2LoadDiTModel, TextEncodeBooguEdit, UNETLoader, CLIPLoader, LoraLoaderModelOnly, SaveImage, SeedVR2LoadVAEModel, LoadImage, EmptyLatentImage, CR Prompt Text, SaveImage, VAEDecode, SeedVR2VideoUpscaler, PrimitiveInt]
patterns: []
missing: [CR Prompt Text]
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Boogu+vr2.5_光学眼镜场景 opticscene_2100503999580565506.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Boogu+vr2.5_光学眼镜场景 opticscene_2100503999580565506.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `VAELoader`
- `SamplerCustom` ★核心
- `DF_Get_image_size`
- `ImageScaleToTotalPixels`
- `KSamplerSelect` ★核心
- `ModelSamplingAuraFlow`
- `BasicScheduler`
- `SeedVR2LoadDiTModel`
- `TextEncodeBooguEdit`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `CR Prompt Text`
- `SaveImage`
- `VAEDecode` ★核心
- `SeedVR2VideoUpscaler`
- `PrimitiveInt`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`VAELoader`、`SamplerCustom`、`DF_Get_image_size`、`ImageScaleToTotalPixels`、`KSamplerSelect`、`ModelSamplingAuraFlow`、`BasicScheduler`、`SeedVR2LoadDiTModel`、`TextEncodeBooguEdit`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`SaveImage`、`SeedVR2LoadVAEModel`、`LoadImage`、`EmptyLatentImage`、`VAEDecode`、`SeedVR2VideoUpscaler`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
