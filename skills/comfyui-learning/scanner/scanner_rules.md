# Workflow Scanner Rules

## 1. Skill Purpose

Workflow Scanner 用于让 AI Agent 自动扫描本地 ComfyUI Workflow 库。

目标：

- Workflow 搜索
- Workflow 分类
- Workflow 推荐
- Workflow 分析
- RAG 知识库构建

## 2. Scanner Input

默认扫描：

```
workflows/
```

支持：

```
.json
.png
.yaml
.yml
```

## 3. Workflow Discovery Rules

Scanner 需要：

1. 递归扫描 workflow 目录
2. 收集 workflow 文件
3. 保存路径、名称、大小、修改时间

## 4. Workflow Parsing

解析 ComfyUI Workflow JSON：

- nodes
- links
- groups
- metadata

重点提取：

- node_type
- class_type
- inputs
- outputs

## 5. Node Dependency Extraction

建立：

Workflow -> Nodes

关系，用于搜索和分析。

## 6. Model Detection

检测 workflow 使用的：

- checkpoint
- diffusion_model
- vae
- lora
- controlnet

## 7. Workflow Fingerprint

根据：

- workflow_name
- node_list
- model_list

生成 workflow_hash，用于去重和相似搜索。

## 8. Scanner Output

生成：

```
workflow_manifest.json
```

## 9. Human Confirmation

Scanner 不负责判断：

- 效果质量
- 艺术风格
- 实际生成效果

这些由人工确认或分析 Skill 处理。

## 10. Agent Usage

扫描完成后 Agent 可以根据：

- 类型
- 节点
- 模型
- 关键词

搜索 Workflow。